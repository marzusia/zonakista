from .base import BaseView
from ..models.articles import Article

class ArticleShowView(BaseView):
    template_name = 'zonakista/article/show.html'

    def get_context_data(self, **kwargs):
        context = super(ArticleShowView, self).get_context_data(**kwargs)
        context['article'] = Article.objects.filter(slug=kwargs['slug']).first()
        return context

class ArticleIndexView(BaseView):
    pass