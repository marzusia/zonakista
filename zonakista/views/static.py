from .base import BaseView
from ..models.articles import Article
from ..models.links import Link

class IndexView(BaseView):
    template_name = 'zonakista/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(
            featured=True,
        ).order_by('-created_at')[:3]
        context['banner'] = Article.objects.filter(
            banner=True,
        ).order_by('-created_at').first()
        context['links'] = Link.objects.all().order_by('title')
        return context
