from django.db import models
from django.urls import reverse
from .base.abstracts import UpdatableModel
from .base.mixins import AutoSlugMixin


class Article(UpdatableModel, AutoSlugMixin):
    title = models.CharField(
        verbose_name='Headline',
        help_text='The headline of the article.',
        max_length=255
    )
    body = models.TextField(
        help_text='The main body of the article'
    )
    slug = models.SlugField(
        max_length=255,
        null=False,
        blank=True,
        db_index=True,
        unique=True,
        help_text='How this article will appear in URLs (leave blank for auto)'
    )
    summary = models.TextField(
        help_text='A short summary of the article for the homepage or article browse page.'
    )
    thumbnail = models.ImageField(
        null=True,
        blank=True,
        help_text='The image to appear with the article',
        upload_to='articles/'
    )
    action_text = models.CharField(
        max_length=64,
        help_text='The text to appear on the button to see the full article.',
        default='Kalya ami'
    )
    public = models.BooleanField(
        default=True,
        help_text='Is this article searchable in the articles page?'
    )
    featured = models.BooleanField(
        default=True,
        help_text='If recent, will this article be visible on the homepage?'
    )
    banner = models.BooleanField(
        default=False,
        help_text='Should this article appear as a banner on the homepage?'
    )

    auto_slug_populate_from = 'title'

    def get_absolute_url(self):
        return reverse('article.show', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title