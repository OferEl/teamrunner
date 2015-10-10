
from django.conf.urls import patterns, url
from coach.views import coachview


urlpatterns = patterns('',
#    
    url(
        regex='',
        view=coachview,
        name='coach',
    ),
   
)