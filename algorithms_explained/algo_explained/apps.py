from django.apps import AppConfig


class AlgoExplainedConfig(AppConfig):
    name = 'algorithms_explained.algo_explained'

    verbose_name = "Explain_Algo"

    def ready(self):
        try:
            # noinspection PyUnresolvedReferences
            from . import signals  # noqa F401
        except ImportError:
            pass
