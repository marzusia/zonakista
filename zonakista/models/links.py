from django.db import models
from django.urls import NoReverseMatch, reverse


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
            'The name of the view to which the link should point, or a valid external address beginning with https://'
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

    def is_external(self):
        return self.url.startswith('https://') or self.url.startswith('http://')

    @property
    def full_url(self):
        if self.is_external():
            return self.url

        try:
            kwargs = {}
            if self.slug:
                kwargs['slug'] = self.slug
            return reverse(self.url, kwargs=kwargs)
        except NoReverseMatch:
            return ''

    def __str__(self):
        return self.title
