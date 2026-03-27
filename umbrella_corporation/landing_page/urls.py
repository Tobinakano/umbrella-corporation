from django.urls import path
from .views import index_view, empresa_view, investigacion_view, ubicaciones_view

urlpatterns = [
	path('', index_view, name='index'),
	path('empresa/', empresa_view, name='empresa'),
	path('investigacion/', investigacion_view, name='investigacion'),
	path('ubicaciones/', ubicaciones_view, name='ubicaciones'),
]
