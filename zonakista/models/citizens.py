from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from .base.abstracts import UpdatableModel
from .cities import City
from .organisation import Organisation


class Citizen(UpdatableModel):
    name = models.CharField(
        unique=True,
        max_length=128,
        help_text=_('This citizen\'s full legal name.'),
    )
    pseudonym = models.CharField(
        max_length=128,
        blank=True,
        help_text=_('Another name by which this citizen may be known, formally or informally.'),
    )
    occupation = models.CharField(
        max_length=255,
        blank=True,
        help_text=_('This citizen\'s legal occupation.'),
    )
    organisation = models.ForeignKey(
        Organisation,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars/',
    )
    city = models.ForeignKey(
        City,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text=_('If this citizen has a corresponding user account, it should be linked here to allow them access '
                    'to managing their citizenship.'),
    )
    date_of_birth = models.DateField(
        help_text=_('This citizen\'s date of birth.'),
    )
    citizenship_start = models.DateField(
        help_text=_('The date upon which this individual became a citizen.'),
    )

    def __str__(self):
        return self.name
