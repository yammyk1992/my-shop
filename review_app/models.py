from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator, MaxValueValidator

from django.db import models


class Review(models.Model):
    """Отзыв к товару с указанием рейтинга"""

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments', verbose_name='Покупатель',
                             null=True)
    review = models.TextField(max_length=256, blank=False, verbose_name='Отзыв')
    image = models.ImageField(upload_to='reviews/%Y', null=True, blank=True, verbose_name='Картинка отзыва')
    rating = models.FloatField(validators=[MinValueValidator(1.0), MaxValueValidator(5.0)], help_text="1-5")
    status = models.BooleanField(default=True)
    subject = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.review} - {self.content_object}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
