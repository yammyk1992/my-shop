from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    """Форма отзывов"""

    class Meta:
        model = Review
        fields = ['subject', 'review', 'rating']


class ImageReviewForm(ReviewForm):
    """Класс формы добавление изображение к посту"""
    image = forms.ImageField(
        label='Выберите фотографии(Не более 4)',
        required=False,
        widget=forms.ClearableFileInput(attrs={'multiple': True})
    )

    class Meta(ReviewForm.Meta):
        fields = ReviewForm.Meta.fields + ['image', ]
