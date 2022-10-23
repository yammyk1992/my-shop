from django.shortcuts import redirect, render

from profile_app.models import Profile
from .forms import ImageReviewForm
from django.contrib.contenttypes.models import ContentType

from django.contrib import messages


def add_review(request, *args, **kwargs):
    if request.method == "POST":
        url = request.META.get('HTTP_REFERER')
        form = ImageReviewForm(request.POST or None, request.FILES)
        image = request.FILES.getlist('image')
        if len(image) > 5:
            context = {
                "title": "Добавление нового поста",
                "form": form,
                "error": "Максимальное количество фотографии - 5"
            }
            return render(request, "product/product_detail.html", context)

        if form.is_valid():
            ct_model, product_slug = kwargs.get('ct_model'), kwargs.get('slug')
            content_type = ContentType.objects.get(model=ct_model)
            product = content_type.model_class().objects.get(slug=product_slug)
            data = form.save(commit=False)
            data.review = request.POST['review']
            data.rating = request.POST['rating']
            data.user = Profile.objects.get(user=request.user)
            data.content_type = content_type
            data.object_id = product.id
            data.save()

            messages.success(request, 'Спасибо, вы добавили отзыв!!!')

            return redirect(url)
