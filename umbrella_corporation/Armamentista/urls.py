from django.urls import path
<<<<<<< HEAD
from .views import armamentista_legal_view

urlpatterns = [
    path('', armamentista_legal_view, name='armamentista_legal'),
=======
from . import views

urlpatterns = [
    path('', views.index, name='index'),
>>>>>>> e77830f40f162c557a4bf9ec852f903884fded35
]
