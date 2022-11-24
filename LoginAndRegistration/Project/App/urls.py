from django.urls import path
from . import views

# Create urls from Here.

urlpatterns = [
    path("", views.home)
]