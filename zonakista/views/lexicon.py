from django.shortcuts import get_object_or_404

from .base import BaseView
from ..models.lexicon import Word


class DictionaryView(BaseView):
    template_name = 'zonakista/lexicon/index.html'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'words': Word.objects.order_by('headword'),
        }


class WordView(BaseView):
    template_name = 'zonakista/lexicon/show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return {
            **super().get_context_data(**kwargs),
            'word': get_object_or_404(Word, slug=kwargs.pop('slug')),
        }
