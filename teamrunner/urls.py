from django.conf.urls import patterns, include, url
from django.contrib import admin
from teamrunner.views import main_page , LoginView,signupView,coachView,groupsView,partnersView
#from teamrunner import account
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teamrunner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r"^index/$", main_page.as_view(),name='index' ),
    #url(r"^signin/$", LoginView.as_view() , name='signin'  ),
    url(r"^signin/", include('account.urls' ),name='signin' ),
    
    #url(r'^author-polls/', include('polls.urls', namespace='author-polls', app_name='account')),
    
    url(r"^signup/$", signupView.as_view() , name='signup'  ),
    url(r"^coach/$", coachView.as_view() , name='coach'  ),
    url(r"^groups/$", groupsView.as_view() , name='groups'  ),
    url(r"^partners/$", partnersView.as_view() , name='partners'),
)
