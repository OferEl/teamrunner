from groups.models import groups
from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf

def groupsview (Request):
    return render(Request,"groups.html",{'entries': groups.objects.values()})