from django.forms import ModelForm

from .models import Product


class ProductAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = "Загружать не более 4 фотографий"


class ImageForm(ModelForm):
    class Meta:
        model = Product
        fields = ['image']