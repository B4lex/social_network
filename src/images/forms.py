from django import forms
from .models import Image

class ImagesForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title', 'image', 'desciption')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(),
            'desciption': forms.Textarea(attrs={'class': 'form-control'}),
        }






