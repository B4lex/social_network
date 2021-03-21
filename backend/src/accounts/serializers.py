from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from accounts.models import ExtendedUser
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class SignInSerializer(TokenObtainPairSerializer):    
    class Meta:
        model = ExtendedUser
        fields = ('username', 'password')
    
    def validate(self, attrs):
        username = attrs.get('username', '')
        user = ExtendedUser.objects.get(username=username)
        if user.is_verified:
            return super().validate(attrs)
        else:
            raise serializers.ValidationError(
                'The username can`t authorization '
            )


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=ExtendedUser.objects.all())]
            )
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True,)

    class Meta:
        model = ExtendedUser
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        elif not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphanumeric '
            )
        else:
            del attrs['password2']
            return super().validate(attrs)

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user