from django.contrib.auth import views
from django.urls import reverse

class LoginView(views.LoginView):
    template_name = 'zonakista/auth/login.html'

class LogoutView(views.LogoutView):
    next_page = 'index'