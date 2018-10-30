from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
#    path('', views.index, name='index'),
    path('', views.index, {'pagename': ''}, name='home'),
    path('<str:pagename>', views.index, name='index'),
]
