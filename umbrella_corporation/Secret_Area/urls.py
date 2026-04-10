from django.urls import path
from . import views

app_name = 'Secret_Area'

urlpatterns = [
    path('', views.index, name='index'),
    path('landing/', views.landing, name='landing'),
    path('empresa/', views.empresa, name='empresa'),
    path('investigacion/', views.investigacion, name='investigacion'),
    path('ubicaciones/', views.ubicaciones, name='ubicaciones'),
]
