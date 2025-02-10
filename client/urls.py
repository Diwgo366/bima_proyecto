from django.urls import path
from client import views

urlpatterns = [
    path('registro/', views.index, name='registro'),
    path('historial/', views.historial, name='historial'),
    path('receive_data/', views.receive_data, name='receive_data'),
]