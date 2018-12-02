from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registro/', views.registro, name="registro"),
    path('registro/crear', views.crear, name="crear"),
    path('registro/listar/', views.listar, name="listar"),
    path('registro/buscar/<int:rut>', views.buscar, name="buscar"),
    path('registro/eliminar/<int:id>', views.eliminar, name="eliminar"),
    path('registro/editar/<int:id>', views.editar, name="editar"),
    path('registro/edicion/<int:id>', views.edicion, name="edicion")
]