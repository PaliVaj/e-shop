from django.contrib.auth.views import LoginView
from django.shortcuts import render

class SubmittableLoginView(LoginView):
    template_name = 'form.html'

