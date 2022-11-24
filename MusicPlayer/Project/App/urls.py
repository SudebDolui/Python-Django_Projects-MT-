from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home),
    path('playlist/', views.playlist),
    path('controls/<str:song>/', views.controls)
]