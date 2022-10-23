from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.dispatch import receiver

from .models import Profile


# сигнал для сохранения создаваемого пользователя в базу и для редактирования пользователя

# Определим сигналы, чтобы наша модель Profile автоматически обновлялась при создании/изменении данных модели User.
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, *args, **kwargs):
    if not created:
        return

    profile = Profile(user=instance)
    profile.save()
