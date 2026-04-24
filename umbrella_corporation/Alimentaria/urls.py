from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_alimentaria, name='index'),
]
