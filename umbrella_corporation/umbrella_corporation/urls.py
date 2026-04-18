"""
URL configuration for umbrella_corporation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('borrador.urls')),
    path('alimentaria/', include('Alimentaria.urls')),
    path('armamentista/', include('Armamentista.urls')),
    path('farmaceutica/', include('Farmaceutica.urls')),
    path('industrial/', include('Industrial.urls')),
    path('investigacion/', include('Investigacion.urls')),
    path('secret_area/', include('Secret_Area.urls')),
    path('uss/', include('USS.urls')),
    path('accounts/', include('accounts.urls')),
]
