from django.shortcuts import render, HttpResponse

from noticias.models import Post



# Create your views here.




def home(request):

    post = Post.objects.last ()
    post1 = { 'Post': post }
    return render(request, "proyectoccvaapp/home.html", post1)


def quienessomos(request):

    return render(request, "proyectoccvaapp/quienessomos.html") 



#def cursosycapacitaciones(request):

   # return render(request, "proyectoccvaapp/cursosycapacitaciones.html")   
   

#def descargas(request):

   # return render(request, "proyectoccvaapp/descargas.html")

