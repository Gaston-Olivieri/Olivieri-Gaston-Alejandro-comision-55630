from django.contrib import admin
from .models import *

# Registrá aqui tus modelos.

admin.site.register(Transporte)
admin.site.register(Papel)
admin.site.register(Ingreso)
admin.site.register(Salida)
admin.site.register(Pedido)
admin.site.register(Contacto)