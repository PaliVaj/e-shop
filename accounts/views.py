from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy


class SubmittableLoginView(LoginView):
    template_name = 'form.html'
    success_url = reverse_lazy('')


