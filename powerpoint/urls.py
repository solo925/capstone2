from django.urls import path
from . import views

urlpatterns = [
    path('', views.powerpoint_list, name='powerpoint_list'),
    path('upload/', views.powerpoint_upload, name='powerpoint_upload'),
]
