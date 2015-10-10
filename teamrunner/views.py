#from django.shortcuts import render
from django.views.generic import TemplateView


class main_page(TemplateView):
    template_name = "index.html"
    
class signupView(TemplateView):
    template_name = "signup.html"
      
class coachView(TemplateView):
    template_name = "coach.html"
    
class partnersView(TemplateView):
    template_name = "partners.html"
    
class groupsView(TemplateView):
    template_name = "groups.html"