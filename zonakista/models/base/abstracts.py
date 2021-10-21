from django.db import models

class UpdatableModel(models.Model):
    """
    Represents a model that can be created and updated, storing these
    as timestamps.
    """

    updated_at = models.DateTimeField(
        auto_now=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        abstract = True