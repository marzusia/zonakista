from django.db import models
from django.urls import reverse, NoReverseMatch

class Link(models.Model):
    title = models.CharField(
        max_length=128,
        unique=True,
        help_text=(
            'The name of the link as it will appear in the homepage.'
        )
    )
    summary = models.CharField(
        max_length=255,
        blank=True,
        help_text=(
            'A small description of the link, which will appear below the '
            'link\'s title.'
        ),
    )
    url = models.CharField(
        max_length=128,
        help_text=(
            'The name of the view to which the link should point.'
        ),
    )
    slug = models.CharField(
        max_length=255,
        blank=True,
        help_text=(
            'The slug, if any, that should be used for reverse-generating '
            'the link.'
        ),
    )

    @property
    def full_url(self):
        try:
            return reverse(self.url, kwargs={'slug': self.slug or None})
        except NoReverseMatch:
            return ''

    def __str__(self):
        return self.title