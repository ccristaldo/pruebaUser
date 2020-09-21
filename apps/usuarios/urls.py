from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
	
	
	path('registro/', views.RegistroUsuario.as_view(), name='registro'),
	path('editar/', views.ModificarUsuario.as_view(), name='editar'),
	
	]