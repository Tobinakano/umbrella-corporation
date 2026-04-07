from django.urls import path
from .views import armamentista_legal_view

urlpatterns = [
    path('', armamentista_legal_view, name='armamentista_legal'),
]
