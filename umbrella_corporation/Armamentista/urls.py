from django.urls import path
from . import views

urlpatterns = [
    path('legal/', views.index, name='index'),
]