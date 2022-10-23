from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',
                                verbose_name='Пользователь')
    photo = models.ImageField(blank=True, null=True)
    about = models.TextField(max_length=4096, verbose_name='О себе', null=True, blank=True)

    def __str__(self):
        return f'Покупатель: {self.user.username}'

    # меняем язык отображения в админке
    class Meta:
        verbose_name = 'Профиль'
        # для множественного числа
        verbose_name_plural = 'Профили'
        ordering = ['id']
