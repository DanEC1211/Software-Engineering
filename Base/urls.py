from django.urls import path
from . import views

urlpatterns = [
    path('', views.Index, name='Index'),
    path('Home', views.Home, name='Home'),
    path('Alert/ENF', views.ENF, name='ENF'),
    path('Alert/Forbidden', views.Forbidden, name='Forbidden'),
    path('Alert/ISE', views.ISE, name='ISE'),
    path('Alert/SU', views.SU, name='SU'),
    path('Alert/WIP', views.WIP, name='WIP'),
]