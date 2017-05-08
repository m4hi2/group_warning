from django.conf.urls import url
from django.contrib.auth.views import login
from .views import home
from .views import PublicView


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
    url(r'^public/$', PublicView.as_view(), name='public'),
]
