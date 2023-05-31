from django.urls import path
from . import views

urlpatterns = [
    path('maths', views.maths, name='maths'),
    path('stat',views.stat,name='stat'),
    path('commerce',views.commerce,name='commerce'),
    path('english',views.english,name='english'),
    path('eco',views.eco,name='eco'),


]