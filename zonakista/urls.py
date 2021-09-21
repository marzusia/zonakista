"""zonakista URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views.profile import ProfileView
from .views.static import IndexView
from .views.article import ArticleShowView, ArticleIndexView
from .views.auth import LoginView, LogoutView
from .views.lexicon import WordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('huzindra', ProfileView.as_view(), name='profile.show'),
    path('idra/<slug:slug>', ArticleShowView.as_view(), name='article.show'),
    path('idra', ArticleIndexView.as_view(), name='article.index'),
    path('gosakokram/<slug:slug>', WordView.as_view(), name='lexicon.show'),
    path('anidaisi', LoginView.as_view(), name='login'),
    path('vidaisi', LogoutView.as_view(), name='logout'),
    path('', IndexView.as_view(), name='index'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )