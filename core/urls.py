from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    # Add more paths as needed
]
