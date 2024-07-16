from django.urls import path
from . import views

urlpatterns = [
    path('', views.photo_essay_list, name='photo_essays'),
    path('create/', views.photo_essay_create, name='photo_essay_create'),
    path('<int:pk>/', views.photo_essay_detail, name='photo_essay_detail'),
]
