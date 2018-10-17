from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Persona
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.

def index(request):
    usuario = request.session.get('usuario',None)
    return render(request,'index.html',{'name':'Registro de personas','personas':Persona.objects.all(),'usuario':usuario})

def crear(request):
    nombre = request.POST.get('nombre','')
    correo = request.POST.get('correo','')
    contrasenia = request.POST.get('contrasenia','')
    persona = Persona(nombre=nombre,correo=correo,contrasenia=contrasenia)
    persona.save()
    return redirect('index')

def eliminar(request,id):
    persona = Persona.objects.get(pk = id)
    persona.delete()
    return redirect('index')

def editar(request):
    nombre = request.POST.get('nombre','')
    correo = request.POST.get('correo','')
    id = request.POST.get('id',0)
    persona = Persona.objects.get(pk = id)
    persona.nombre = nombre
    persona.correo = correo
    persona.save()
    return redirect('index')

def cerrar_session(request):
    del request.session['usuario']
    return redirect('index')

def login(request):
    return render(request,'login.html',{})

def login_iniciar(request):
    nombre_usuario = request.POST.get('nombre_usuario','')
    contrasenia = request.POST.get('contrasenia','')
    persona = authenticate(username=nombre_usuario, password=contrasenia)
    if persona is not None:
        request.session['usuario'] = persona.first_name+" "+persona.last_name
        return redirect('index')
    else:
        return redirect('index')
    