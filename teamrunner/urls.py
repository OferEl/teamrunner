from django.conf.urls import patterns, include, url
from django.contrib import admin
from teamrunner.views import main_page , LoginView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teamrunner.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r"^index/$", main_page.as_view()),
    url(r"^login/$", LoginView.as_view() , name='login'  ),
)
