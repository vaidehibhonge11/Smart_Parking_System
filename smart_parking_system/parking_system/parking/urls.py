from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehicle-entry/', views.vehicle_entry, name='vehicle_entry'),
    path('vehicle-exit/', views.vehicle_exit, name='vehicle_exit'),
]
