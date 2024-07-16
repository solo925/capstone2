from django.urls import path
from . import views

urlpatterns = [
    path('', views.autobiography_list, name='autobiography-view'),
     path('create/', views.autobiography_create, name='autobiography_create'),
    path('<int:pk>/', views.autobiography_detail, name='autobiography_detail'),
    
]