from django.contrib import admin
from django.utils.safestring import mark_safe

from .forms import ProductAdminForm
from .models import Sport, TV, Toys, Goods, ImageSportProducts, ImageTVProducts, ImageGoodsProducts, ImageToysProducts

admin.site.register(ImageToysProducts)
admin.site.register(ImageSportProducts)
admin.site.register(ImageTVProducts)
admin.site.register(ImageGoodsProducts)


class SportImageAdmin(admin.StackedInline):
    model = ImageSportProducts
    # readonly_fields = ('image_preview',)
    verbose_name = "Фотография к cпортивному товару"
    list_display = ('__all__',)
    verbose_name_plural = "Фотографии к спортивным товарам"

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<a href="{obj.image.url}">'
                f'<img src="{obj.image.url}" width ="150" height="150" />'
                f'</a>'
            )

    image_preview.short_description = 'Фото к товару'
    image_preview.allow_tags = True


@admin.register(Sport)
class SportProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image_preview')
    prepopulated_fields = {'slug': ('name',)}

    inlines = (
        SportImageAdmin,
    )

    form = ProductAdminForm

    def image_preview(self, obj):
        # ex. the name of column is "image"
        if obj.image:
            return mark_safe(
                '<img src="{0}" width="80" height="50" style="object-fit:contain" />'.format(obj.image.url))
        else:
            return 'Нет картинки'

    image_preview.short_description = 'Фото к товару'
    image_preview.allow_tags = True


class TVImageAdmin(admin.StackedInline):
    model = ImageTVProducts
    # readonly_fields = ('image_preview',)
    verbose_name = "Фотография к cпортивному товару"
    list_display = ('__all__',)
    verbose_name_plural = "Фотографии к спортивным товарам"

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<a href="{obj.image.url}">'
                f'<img src="{obj.image.url}" width ="150" height="150" />'
                f'</a>'
            )

    image_preview.short_description = 'Фото к товару'
    image_preview.allow_tags = True


@admin.register(TV)
class TVProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image_preview')
    prepopulated_fields = {'slug': ('name',)}

    inlines = (
        TVImageAdmin,
    )

    form = ProductAdminForm

    def image_preview(self, obj):
        # ex. the name of column is "image"
        if obj.image:
            return mark_safe(
                '<img src="{0}" width="80" height="50" style="object-fit:contain" />'.format(obj.image.url))
        else:
            return 'Нет картинки'

    image_preview.short_description = 'Фото к товару'
    image_preview.allow_tags = True


class GoodsImageAdmin(admin.StackedInline):
    model = ImageGoodsProducts
    # readonly_fields = ('image_preview',)
    verbose_name = "Фотография к cпортивному товару"
    list_display = ('__all__',)
    verbose_name_plural = "Фотографии к спортивным товарам"

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<a href="{obj.image.url}">'
                f'<img src="{obj.image.url}" width ="150" height="150" />'
                f'</a>'
            )

    image_preview.short_description = 'Фото к товару'
    image_preview.allow_tags = True


@admin.register(Goods)
class GoodsProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image_preview')
    prepopulated_fields = {'slug': ('name',)}

    inlines = (
        GoodsImageAdmin,
    )

    form = ProductAdminForm

    def image_preview(self, obj):
        # ex. the name of column is "image"
        if obj.image:
            return mark_safe(
                '<img src="{0}" width="80" height="50" style="object-fit:contain" />'.format(obj.image.url))
        else:
            return 'Нет картинки'

    image_preview.short_description = 'Фото к товару'
    image_preview.allow_tags = True


class ToysImageAdmin(admin.StackedInline):
    model = ImageToysProducts
    # readonly_fields = ('image_preview',)
    verbose_name = "Фотография к cпортивному товару"
    list_display = ('__all__',)
    verbose_name_plural = "Фотографии к спортивным товарам"

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<a href="{obj.image.url}">'
                f'<img src="{obj.image.url}" width ="150" height="150" />'
                f'</a>'
            )

    image_preview.short_description = 'Фото к товару'
    image_preview.allow_tags = True


@admin.register(Toys)
class ToysProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image_preview')
    prepopulated_fields = {'slug': ('name',)}

    inlines = (
        ToysImageAdmin,
    )

    form = ProductAdminForm

    def image_preview(self, obj):
        # ex. the name of column is "image"
        if obj.image:
            return mark_safe(
                '<img src="{0}" width="80" height="50" style="object-fit:contain" />'.format(obj.image.url))
        else:
            return 'Нет картинки'

    image_preview.short_description = 'Фото к товару'
    image_preview.allow_tags = True
