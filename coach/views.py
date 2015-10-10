from coach.models import coach
from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf

def coachview (Request):
    return render(Request,"coach.html",{'entries': coach.objects.values()})