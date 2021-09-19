from django.apps import AppConfig

class ZonakistaConfig(AppConfig):
    name = 'zonakista'
    verbose_name = 'Zonakista Vezas'

    def ready(self):
        from . import signals
