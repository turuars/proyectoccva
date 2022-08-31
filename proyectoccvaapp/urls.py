from django.urls import path
from proyectoccvaapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home, name="Home"),
    path("quienessomos/",views.quienessomos, name="QuienesSomos"),
    #path("cursosycapacitaciones/",views.cursosycapacitaciones, name="CursosyCapacitaciones"),
    #path("descargas/",views.descargas, name="Descargas"),

]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
