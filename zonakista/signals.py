from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models.base.mixins import AutoSlugMixin
from .utils.models import base_receiver

@base_receiver(pre_save, sender=AutoSlugMixin)
def add_auto_slug(sender, instance, **kwargs):
    instance.hydrate_slug()