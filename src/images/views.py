from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from .models import Image
from .forms import ImagesForm
import json


@login_required
def list_images(request):
    images = Image.objects.all()
    return render(request, 'images/list_image.html', {'images': images})

@login_required
def image_create(request):
    data = dict()
    if request.method == 'POST':

        form = ImagesForm(request.POST, request.FILES)

        print(form)
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            images = Image.objects.all()
            data['html_image_list'] = render_to_string('images/list.html', {
                'images': images
            })
        else:
            data['form_is_valid'] = False
    else:
        form = ImagesForm()
    context = {'form': form}
    data['html_form'] = render_to_string('images/image/create.html', context, request=request)
    return HttpResponse(json.dumps(data), content_type="application/json")


# @login_required
# def image_create(request):
#     if request.method == 'POST':
#         form = ImagesForm(data=request.POST, files=request.FILES)
#
#         print(request.FILES)
#     else:
#         form = ImagesForm()
#     return save_image_form(request, form, 'images/image/create.html')