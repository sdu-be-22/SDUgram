from django.apps import AppConfig


class MyProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myProfile'

    def ready(self):
        import myProfile.signals  # noqa
