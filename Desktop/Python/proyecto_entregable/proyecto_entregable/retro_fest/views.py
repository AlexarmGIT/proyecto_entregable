from django.shortcuts import render
from retro_fest.models import Familia 
from retro_fest.models import Amigos 
from retro_fest.models import Conocidos 
from django.http import HttpResponse
import datetime

# Create your views here.


def inicio(request):
    return render (request , "inicio.html")



def lista_familia (request):
    familiares = Familia.objects.all()
    datos = {"datos" : familiares }   

    return render (request , "lista_invitados.html" , datos)


def alta_familiares (request):
    familiar = Familia( nombre= "Paz" , parentezco= "hija" , edad=4 )
    familiar.save()
    familiar = Familia( nombre= "Alfonsina" , parentezco= "hija"  , edad=1 )
    familiar.save()
    familiar = Familia( nombre= "Antonella" , parentezco= "Conyuge" , edad=31 )
    familiar.save()

def lista_amigos (request):
    amistades = Amigos.objects.all()
    datos = {"datos" : amistades }   

    return render (request , "lista_invitados.html" , datos)


def alta_amistades (request):
    amistad = Amigos( nombre= "Martin" , amigo_de= "Escuela" , edad=31 )
    amistad.save()
    amistad = Amigos( nombre= "Fidel" , amigo_de= "Escuela" , edad=31 )
    amistad.save()
    amistad = Amigos( nombre= "Augusto" , amigo_de= "Escuela" , edad=31 )
    amistad.save()

def lista_conocidos (request):
    compinches = Conocidos.objects.all()
    datos = {"datos" : compinches }   

    return render (request , "lista_invitados.html" , datos)

def alta_conocidos (request):
    conocido = Conocidos( nombre= "Marcos" , conocido_de= "Futbol" ,  edad=27 )
    conocido.save()
    conocido = Conocidos( nombre= "lucas" , conocido_de= "Gym" , edad=37 )
    conocido.save()
    conocido = Conocidos( nombre="pablo" , conocido_de= "basquet" , edad=22 )
    conocido.save()


    return HttpResponse("Se ha ejecutado correctamente")