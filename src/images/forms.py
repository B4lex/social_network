# from django import forms
# from .models import Image
#
# from urllib import request
# from django.core.files.base import ContentFile
# from django.utils.text import slugify
#
# class ImageCreateForm(forms.ModelForm):
#     class Meta:
#         model = Image
#         fields = ('title', 'url', 'desciption')
#         widgets = {'url': forms.HiddenInput,}
#
#     def clean_url(self):
#         url = self.cleaned_data['url']
#         valid_extensions = ['jpg', 'jpeg', 'png']
#         extensions = url.rsplit('.', 1)[1].lower()
#         if extensions not in valid_extensions:
#             raise forms.ValidationError('The given Url does not\n'
#                                         'math valid image extensions.')
#
#     def save(self, force_insert=False, force_update=False, commit=True):
#         image = super(ImageCreateForm, self).save(commit=False)
#         image_url = self.cleaned_data['url']
#         image_name = '{}.{}'.format(slugify(image.title), image_url.rsplit('.',1)[1].lower())
#         response = request.urlopen(image_url)
#         image.image.save(image_name, ContentFile(response.read()), save=False)
#         if commit:
#             image.save()
#         return image

from django import forms
from .models import Image

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('user', 'title', 'image', 'desciption')
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control'}),
        #     'image': forms.FileField(),
        #     'desciption': forms.Textarea(attrs={'class': 'form-control'}),
        # }



