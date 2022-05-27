from django.http import HttpResponse
from django.shortcuts import render
from app_coder.models import Curso

# Create your views here.

def cursos(request):
    cursos = Curso.objects.all()

    return HttpResponse( cursos )

def alta_curso(request, cursos):
    curso = Curso(request.nombre , request.camada)
    curso.save()
    texto = f"Se guardo en la BD el Curso: {curso.nombre} Camada: {curso.camada}"
    return HttpResponse(texto)
    
