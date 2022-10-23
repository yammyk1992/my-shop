from django.apps import AppConfig


class ProfileAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profile_app'

    # применяем сигнал
    def ready(self):
        from profile_app import signals
