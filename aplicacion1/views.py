from django.shortcuts import render

from .models import *
from .forms import *

from django.urls import reverse_lazy
from django.http import HttpResponse

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Views de la aplicacion 

@login_required
def inicio(request):
    return render(request, "aplicacion1/inicio.html")

@login_required
def transportistas(request):
    contexto = {'transportistas': Transporte.objects.all() }
    return render(request, "aplicacion1/transportistas.html", contexto)

def contactos(request):
    contexto = {'contactos': Contacto.objects.all() }
    return render(request, "aplicacion1/contactos.html", contexto)

def AcercaDeMi(request):
    contexto = {'AcercaDeMi': Contacto.objects.all() }
    return render(request, "aplicacion1/AcercaDeMi.html", contexto)

# Buscar:

@login_required
def buscar(request):
    if request.GET['Buscar']:
        patron = request.GET['Buscar']
        transportistas = Transporte.objects.filter(transportista__icontains=patron)
        contexto = {"transportistas":transportistas}
        return render(request, "aplicacion1/transportistas.html", contexto)
    return HttpResponse("Debe ingresar palabra o letra")


# Class Based View Papeles:

class PapelList(LoginRequiredMixin, ListView):
    model = Papel

class PapelCreate(LoginRequiredMixin, CreateView):
    model = Papel
    fields = ['transportista', 'cuit_transporte', 'chofer', 'cuit_chofer', 'patente_chasis', 'tecnica_chasis', 'ruta_chasis', 'seguro_chasis', 'patente_acoplado', 'tecnica_acoplado', 'ruta_acoplado', 'seguro_acoplado', 'seguro_carga', 'importe', 'licencia', 'psicofisico', 'cuota_sindical', 'art', 'seguro_vida', 'telefono' ]
    success_url = reverse_lazy('papeles')

class PapelUpdate(LoginRequiredMixin, UpdateView):
    model = Papel
    fields = ['transportista', 'cuit_transporte', 'chofer', 'cuit_chofer', 'patente_chasis', 'tecnica_chasis', 'ruta_chasis', 'seguro_chasis', 'patente_acoplado', 'tecnica_acoplado', 'ruta_acoplado', 'seguro_acoplado', 'seguro_carga', 'importe', 'licencia', 'psicofisico', 'cuota_sindical', 'art', 'seguro_vida', 'telefono' ]
    success_url = reverse_lazy('papeles')

class PapelDelete(LoginRequiredMixin ,DeleteView):
    model = Papel
    success_url = reverse_lazy('papeles')


# Class Based View Pedidos:

class PedidoList(LoginRequiredMixin, ListView):
    model = Pedido

class PedidoCreate(LoginRequiredMixin, CreateView):
    model = Pedido
    fields = ['fecha', 'sucursal', 'cuenta', 'horario', 'ubicacion', 'transportista', 'cumplimiento', 'observacion' ]
    success_url = reverse_lazy('pedidos')

class PedidoUpdate(LoginRequiredMixin, UpdateView):
    model = Pedido
    fields = ['fecha', 'sucursal', 'cuenta', 'horario', 'ubicacion', 'transportista', 'cumplimiento', 'observacion' ]
    success_url = reverse_lazy('pedidos')

class PedidoDelete(LoginRequiredMixin ,DeleteView):
    model = Pedido
    success_url = reverse_lazy('pedidos')


# Class Based View Ingresos:

class IngresoList(LoginRequiredMixin, ListView):
    model = Ingreso

class IngresoCreate(LoginRequiredMixin, CreateView):
    model = Ingreso
    fields = ['fecha', 'cuenta', 'cpe', 'chofer', 'grano', 'humedad_chasis', 'humedad_acoplado', 'promedio', 'bruto', 'tara', 'neto', 'observacion', 'ticket' ]
    success_url = reverse_lazy('ingresos')

class IngresoUpdate(LoginRequiredMixin, UpdateView):
    model = Ingreso
    fields = ['fecha', 'cuenta', 'cpe', 'chofer', 'grano', 'humedad_chasis', 'humedad_acoplado', 'promedio', 'bruto', 'tara', 'neto', 'observacion', 'ticket' ]
    success_url = reverse_lazy('ingresos')

class IngresoDelete(LoginRequiredMixin, DeleteView):
    model = Ingreso
    success_url = reverse_lazy('ingresos')


# Class Based View Salidas:

class SalidaList(LoginRequiredMixin, ListView):
    model = Salida

class SalidaCreate(LoginRequiredMixin, CreateView):
    model = Salida
    fields = ['fecha', 'grano', 'cupo', 'cpe', 'transportista', 'bruto', 'tara', 'neto', 'observacion']
    success_url = reverse_lazy('salidas')

class SalidaUpdate(LoginRequiredMixin, UpdateView):
    model = Salida
    fields = ['fecha', 'grano', 'cupo', 'cpe', 'transportista', 'bruto', 'tara', 'neto', 'observacion']
    success_url = reverse_lazy('salidas')

class SalidaDelete(LoginRequiredMixin, DeleteView):
    model = Salida
    success_url = reverse_lazy('salidas')


#Login / Logout / Registracion:

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            contraseña = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.jpg"
                finally:
                    request.session["avatar"] = avatar
                    
                return render(request, "aplicacion1/inicio.html")
            else:
                return render(request, "aplicacion1/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplicacion1/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion1/login.html", {'form': miForm}) 

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion1/registroaprobado.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion1/registrarse.html", {"form":miForm})   

#Editar Perfil:

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.save()
            return render(request,"aplicacion1/editaraprobado.html")
        else:
            return render(request,"aplicacion1/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion1/editarPerfil.html", {'form': form, 'usuario': usuario.username})

@login_required
def nuevoAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) 
        if form.is_valid():
            usuario = User.objects.get(username=request.user)

            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            avatar = Avatar(user=usuario, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion1/avataraprobado.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion1/nuevoAvatar.html", {'form': form })