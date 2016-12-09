from django.conf.urls import url
from django.contrib.auth.views import login
from .views import home


urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^login/$', login, {'template_name': 'login.html'}, name='login'),
]
