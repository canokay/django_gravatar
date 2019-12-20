from django.conf.urls import url

from django.urls import path,include
from django.conf.urls import url

from django_gravatar.views import LoginView, IndexView

app_name = 'django_gravatar'

urlpatterns = [
    url(r'^$', IndexView, name='homepage'),
    url(r'^login/$', LoginView, name='login'),
]