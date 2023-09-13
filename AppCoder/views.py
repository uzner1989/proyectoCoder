from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Profesor
from AppCoder.models import Curso

# Create your views here.

def profe_nuevo(request):
    profeN = Profesor(nombre="Pepe", apellido="Python", email="pepe@python.com", profesion="biologo")
    profeN.save()

    return HttpResponse(f"Hemos guardado al profesor {profeN.nombre}")


def curso_nuevo(request):
    mi_curso_favorito = Curso(nombre="Python", camada=47765 )
    mi_curso_favorito.save()

    return HttpResponse(f"Bienvenidos al curso {mi_curso_favorito.nombre}")