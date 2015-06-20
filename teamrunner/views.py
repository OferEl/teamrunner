#from django.shortcuts import render
from django.views.generic import TemplateView, FormView


class main_page(TemplateView):
    template_name = "index.html"
    
    
class LoginView(TemplateView):
    template_name = "signin.html"
    
class signupView(TemplateView):
    template_name = "signup.html"
    
class coachView(TemplateView):
    template_name = "coach.html"
    
class groupsView(TemplateView):
    template_name = "coach.html"
    
class partnersView(TemplateView):
    template_name = "coach.html"