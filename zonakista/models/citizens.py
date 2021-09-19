from zonakista.models.organisation import Organisation
from django.db import models
from django.contrib.auth.models import User
from .base.abstracts import UpdatableModel
from .cities import City
from .organisation import Organisation

class Citizen(UpdatableModel):
    name = models.CharField(unique=True, max_length=128)
    occupation = models.CharField(max_length=255)
    organisation = models.ForeignKey(
        Organisation,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    avatar = models.ImageField(
        null=True,
        blank=True,
        upload_to='avatars/'
    )
    city = models.ForeignKey(
        City,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    citizenship_start = models.DateField()

    def __str__(self):
        return self.name