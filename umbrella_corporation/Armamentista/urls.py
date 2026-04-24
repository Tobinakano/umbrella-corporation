from django.urls import path
from . import views

urlpatterns = [
    path('legal/', views.index_legal, name='index_legal'),
    path('ilegal/', views.index_ilegal, name='index_ilegal'),
]
