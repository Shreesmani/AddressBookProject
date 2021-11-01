from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index',),
    path('addaddress', views.addaddress, name='addaddress'),
    path('viewaddress', views.viewaddress, name='viewaddress')
]
