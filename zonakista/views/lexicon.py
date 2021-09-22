from .base import BaseView
from ..models.lexicon import Word

class DictionaryView(BaseView):
    template_name = 'zonakista/lexicon/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['words'] = Word.objects.all()
        return context

class WordView(BaseView):
    template_name = 'zonakista/lexicon/show.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['word'] = Word.objects.filter(slug=kwargs['slug']).first()
        return context