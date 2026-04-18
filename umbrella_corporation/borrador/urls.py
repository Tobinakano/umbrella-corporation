from django.urls import path
from .views import index_view, empresa_view, investigacion_view, ubicaciones_view
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
	path('', index_view, name='index'),
	path('empresa/', empresa_view, name='empresa'),
	path('investigacion/', investigacion_view, name='investigacion'),
	path('ubicaciones/', ubicaciones_view, name='ubicaciones'),
	path('quick_register/', index_view, name='quick_register'),
]
