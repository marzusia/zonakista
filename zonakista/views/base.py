from django.views.generic import TemplateView
from ..models.citizens import Citizen

class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['citizen'] = Citizen.objects.filter(
                user=self.request.user).first()
        return context