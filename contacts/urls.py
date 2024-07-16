from django.urls import path
from .import views

urlpatterns = [
    path('', views.contact_view, name='contacts'),
    path('edit/', views.contact_edit, name='contact_edit'),
]
