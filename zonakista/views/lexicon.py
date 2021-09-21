from .base import BaseView
from ..models.lexicon import Word

class WordView(BaseView):
    template_name = 'zonakista/lexicon/word.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['word'] = Word.objects.filter(slug=kwargs['slug']).first()
        return context