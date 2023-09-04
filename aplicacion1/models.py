from django.db import models
from django.contrib.auth.models import User

# Mis Modelos

class Transporte(models.Model):
    transportista = models.CharField(max_length=100)
    cuit_transporte = models.IntegerField()
    chofer = models.CharField(max_length=100)
    cuit_chofer = models.IntegerField()
    patente_chasis = models.CharField(max_length=10)
    patente_acoplado = models.CharField(max_length=10)
    observacion = models.CharField(max_length=250)
   
    class Meta:
        verbose_name = "Transportista"
        verbose_name_plural = "Transportistas"
        
    def __str__(self):
        return f"{self.transportista}"
    
class Papel(models.Model):
    transportista = models.CharField(max_length=100)
    cuit_transporte = models.IntegerField()
    chofer = models.CharField(max_length=100)
    cuit_chofer = models.IntegerField()
    patente_chasis = models.CharField(max_length=10)
    tecnica_chasis = models.CharField(max_length=10)
    ruta_chasis = models.CharField(max_length=10)
    seguro_chasis = models.CharField(max_length=10)
    patente_acoplado = models.CharField(max_length=10)
    tecnica_acoplado = models.CharField(max_length=10)
    ruta_acoplado = models.CharField(max_length=10)
    seguro_acoplado = models.CharField(max_length=10)
    seguro_carga = models.CharField(max_length=10)
    importe = models.CharField(max_length=10)
    licencia = models.CharField(max_length=10)
    psicofisico = models.CharField(max_length=10)
    cuota_sindical = models.CharField(max_length=10)
    art = models.CharField(max_length=10)
    seguro_vida = models.CharField(max_length=10)
    telefono = models.IntegerField()
   
    class Meta:
        verbose_name = "Papel"
        verbose_name_plural = "Papeles"
        
    def __str__(self):
        return f"{self.transportista}"
    
    
class Pedido(models.Model):
    fecha = models.CharField(max_length=10, blank=False)
    sucursal = models.CharField(max_length=15, blank=False)
    cuenta = models.CharField(max_length=100, blank=False)
    horario = models.CharField(max_length=5, blank=False)
    ubicacion = models.CharField(max_length=500, blank=False)
    transportista = models.CharField(max_length=100)
    cumplimiento = models.CharField(max_length=20)
    observacion = models.CharField(max_length=250)

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return f"{self.cuenta}"
    
class Ingreso(models.Model):
    fecha = models.CharField(max_length=10, blank=False)
    cuenta = models.CharField(max_length=100, blank=False)
    cpe = models.IntegerField(blank=False)
    chofer = models.CharField(max_length=100, blank=False)
    grano = models.CharField(max_length=10, blank=False)
    humedad_chasis = models.CharField(max_length=5, blank=False)
    humedad_acoplado = models.CharField(max_length=5, blank=False)
    promedio = models.CharField(max_length=5, blank=False)
    bruto = models.IntegerField()
    tara = models.IntegerField()
    neto = models.IntegerField()
    observacion = models.CharField(max_length=250)
    ticket = models.IntegerField()

    class Meta:
        verbose_name = "Ingreso"
        verbose_name_plural = "Ingresos"

    def __str__(self):
        return f"{self.cuenta}"
    
class Salida(models.Model):
    fecha = models.CharField(max_length=10, blank=False)
    grano = models.CharField(max_length=10, blank=False)
    cupo = models.CharField(max_length=100, blank=False)
    cpe = models.IntegerField(blank=False)
    transportista = models.CharField(max_length=100)
    bruto = models.IntegerField()
    tara = models.IntegerField()
    neto = models.IntegerField()
    observacion = models.CharField(max_length=250)
  
    class Meta:
        verbose_name = "Salida"
        verbose_name_plural = "Salidas"

    def __str__(self):
        return f"{self.cupo}"

class Contacto(models.Model):
    sucursal = models.CharField(max_length=50)
    direccion = models.CharField(max_length=150)
    horario = models.CharField(max_length=50)
    telefono = models.IntegerField()
    telefono2 = models.IntegerField()

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return f"{self.sucursal}"
    

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}"