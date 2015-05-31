#from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.views.generic import TemplateView, FormView


class main_page(TemplateView):
    template_name = "index.html"
    
    
class LoginView(FormView):
    template_name = 'login.html'
