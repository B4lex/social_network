from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.template.loader import render_to_string
from .models import Image
from .forms import ImagesForm


from images.common.decorators.decoratots import ajax_required


@login_required
def list_images(request):
    images = Image.objects.filter(user_id=request.user)
    return render(request, 'images/list_image.html', {'images': images})


@login_required
def save_image_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            data['form_is_valid'] = True
            images = Image.objects.filter(user_id=request.user)
            data['html_image_list'] = render_to_string('images/list.html', {
                'images': images
            }, request=request)
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


@login_required
def image_create(request):
    if request.method == 'POST':
        form = ImagesForm(data=request.POST, files=request.FILES)
    else:
        form = ImagesForm()
    return save_image_form(request, form, 'images/image/create.html')


@login_required
def images_update(request, pk):
    image = get_object_or_404(Image, pk=pk)
    print('pizdas')
    if request.method == 'POST':
        form = ImagesForm(request.POST, files=request.FILES, instance=image)
    else:

        form = ImagesForm(instance=image)
    return save_image_form(request, form, 'images/image/update.html')


@login_required
def image_delete(request, pk):
    image = get_object_or_404(Image, pk=pk)
    data = dict()
    if request.method == 'POST':
        image.delete()
        data['form_is_valid'] = True
        images = Image.objects.filter(user_id=request.user)
        data['html_image_list'] = render_to_string('images/list.html', {
            'images': images
        }, request=request,)

    else:
        context = {'image': image}
        data['html_form'] = render_to_string('images/image/delete.html',
                                             context,
                                             request=request,)
    return JsonResponse(data)


@login_required
def image_detail(request, pk, slug):
    image = get_object_or_404(Image, id=pk, slug=slug)
    context = {'image': image}
    return render(request,
                  'images/image/detail.html',
                  context)


@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = get_object_or_404(Image, id=image_id)
            if action == 'like':
                image.user_like.add(request.user)
            else:
                image.user_like.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            return JsonResponse({'status': 'error'})


