from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from accounts.serializers import RegisterSerializer, SignInSerializer

from accounts.models import ExtendedUser
from accounts.utils import Util
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.core.mail import send_mail
import jwt
from server import settings
from rest_framework_simplejwt import views as jwt_views


class SignInView(jwt_views.TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = SignInSerializer


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = ExtendedUser.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relativateLink = reverse('accounts:email-verify')
        absurl = f'http://{current_site}{relativateLink}?token={token}'
        email_body = f'Hi  {user.username} \n {absurl}'
        data = {'email_body': email_body,
                'email_subject': "Verify you email",
                'to_email': user.email}
        print(data)
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class VerifyEmail(generics.GenericAPIView):
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            print(payload)
            user = ExtendedUser.objects.get(id=payload['user_id'])        
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'error': 'Successfully activated'}, status=status.HTTP_201_CREATED)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)
