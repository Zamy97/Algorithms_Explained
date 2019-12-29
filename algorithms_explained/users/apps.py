from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "algorithms_explained.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import algorithms_explained.users.signals  # noqa F401
        except ImportError:
            pass
