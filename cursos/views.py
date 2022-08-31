from django.shortcuts import render
from cursos.models import Curso, Tipo

# Create your views here.


def cursos(request):

    cursos=Curso.objects.all()

    return render(request, "cursos/cursos.html", {"cursos": cursos})



def tipo(request, tipo_id):

    tipo=Tipo.objects.get(id=tipo_id)
    tipos=Curso.objects.filter(tipos=tipos)
    return render(request, "cursos/tipos.html", {'tipo':tipo,"cursos": cursos })


