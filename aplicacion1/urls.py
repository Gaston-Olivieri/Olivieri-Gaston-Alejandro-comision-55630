from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name="inicio" ),
    path('transportistas/', transportistas, name="transportistas" ),
    path('contactos/', contactos, name="contactos" ),
    path('AcercaDeMi/', AcercaDeMi, name="AcercaDeMi" ),
    
    # Buscar:
    path('buscar/', buscar, name="buscar" ),
    
    # Class Based View Documentacion:
    path('papeles/', PapelList.as_view(), name="papeles" ),
    path('create_papeles/', PapelCreate.as_view(), name="create_papeles" ),    
    path('update_papeles/<int:pk>/', PapelUpdate.as_view(), name="update_papeles" ),
    path('delete_papeles/<int:pk>/', PapelDelete.as_view(), name="delete_papeles" ),

    # Class Based View pedidos:
    path('pedidos/', PedidoList.as_view(), name="pedidos" ),
    path('create_pedidos/', PedidoCreate.as_view(), name="create_pedidos" ),    
    path('update_pedidos/<int:pk>/', PedidoUpdate.as_view(), name="update_pedidos" ),
    path('delete_pedidos/<int:pk>/', PedidoDelete.as_view(), name="delete_pedidos" ),

    # Class Based View Ingresos:
    path('ingresos/', IngresoList.as_view(), name="ingresos" ),
    path('create_ingresos/', IngresoCreate.as_view(), name="create_ingresos" ),    
    path('update_ingresos/<int:pk>/', IngresoUpdate.as_view(), name="update_ingresos" ),
    path('delete_ingresos/<int:pk>/', IngresoDelete.as_view(), name="delete_ingresos" ),

    # Class Based View Salidas:
    path('salidas/', SalidaList.as_view(), name="salidas" ),
    path('create_salidas/', SalidaCreate.as_view(), name="create_salidas" ),    
    path('update_salidas/<int:pk>/', SalidaUpdate.as_view(), name="update_salidas" ),
    path('delete_salidas/<int:pk>/', SalidaDelete.as_view(), name="delete_salidas" ),

    #Login / Logout / Registracion:
    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion1/logout.html"), name="logout" ),
    path('registrarse/', register, name="registrarse" ),

    #Editar perfil / Agregar Avatar
    path('editar_perfil/', editarPerfil, name="editar_perfil" ),
    path('nuevoAvatar/', nuevoAvatar, name="nuevoAvatar" ),
    
]
