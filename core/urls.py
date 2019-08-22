from django.conf.urls import url
from core import views

urlpatterns = [
url(r'^$', views.Home, name='Home'),
url(r'^login/$', views.Login, name='Login'),
]