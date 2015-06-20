import logging

from django.shortcuts import render_to_response, HttpResponseRedirect
from django.views.generic import FormView
from django.template import RequestContext
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
##from axes.decorators import watch_login
#from braces.views import LoginRequiredMixin

#from .forms import UserSettingsForm, SignUpForm

logger = logging.getLogger(__name__)


#@watch_login
def signin(request):
    # Force logout.
    logout(request)
    username = password = ''
    

    # Flag to keep track whether the login was invalid.
    login_failed = False

    if request.POST:
        username = request.POST['username'].replace(' ', '').lower()
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/index/')
        else:
            login_failed = True

    return render_to_response('accounts/signin.html',
                              {'login_failed': login_failed},
                              context_instance=RequestContext(request))


