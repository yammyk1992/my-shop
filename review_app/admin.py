from django.contrib import admin

from .models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('user', 'rating', 'created_at', 'content_object', 'image')
