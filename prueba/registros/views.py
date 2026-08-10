from django.shortcuts import render, get_object_or_404
from .models import Alumnos, ComentarioContacto #Accedemos al modelo Alumnos que contiene la estructura de la tabla.
from .models import Comentario, Archivos
from .forms import ComentarioContactoForm, FormArchivos
import datetime
from datetime import date
from django.contrib import messages


# Create your views here.
def registros(request):
    alumnos = Alumnos.objects.all() # all recuperar todos los objetos del modelo (registros de la tabla alumnos)
    comentario = Comentario.objects.all()
    
    return render(request, "registros/principal.html", {'alumnos': alumnos})
    #indicamso el lugar donde se renderiza el resultado de esta vista y enviamos la lista de alumnos recuperados

def Consultas(request):
    alumnos = Alumnos.objects.all() # all recuperar todos los objetos del modelo (registros de la tabla alumnos)
    comentario = Comentario.objects.all()
    
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, 'registros/consultar_comentarios.html', {'comentarios': comentarios})
    form = ComentarioContactoForm()
    #Si sale mal reenvian al formulario los datos ingresados
    return render(request, 'registros/contacto.html', {'form': form})

def contacto(request):
    return render(request, "registros/contacto.html")

def consultar_comentarios(request):
    comentarios = ComentarioContacto.objects.all()

    return render(
        request,
        "registros/consultar_comentarios.html",
        {"comentarios": comentarios}
    )

def eliminarComentarioContacto(request, id, confirmacion='registros/confirmarEliminacion.html'):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultar_comentarios.html", {'comentarios': comentarios})
    return render(request, confirmacion, {'comentario': comentario})

def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)

    if request.method == "POST":
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request,"registros/consultar_comentarios.html",{"comentarios": comentarios})
    else:
        form = ComentarioContactoForm(instance=comentario)
    return render(request,"registros/editarComentario.html",{"form": form,"comentario": comentario})

def consultar1(request):
    #con una sola condicion
    alumnos = Alumnos.objects.filter(carrera="TI") 
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar2(request):
    #con una sola condicion
    alumnos = Alumnos.objects.filter(carrera="TI").filter(turno="Matutino") 
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar3(request):
    #si solo deseamos recuperar ciertos datos agregamos la funcion only, listando los campos que deseamos recuperar
    #de la consulta emplear filter() o en el ejemplo all()
    alumnos = Alumnos.objects.all().only("matricula","nombre","imagen")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar4(request):
    alumnos = Alumnos.objects.filter(nombre__icontains="Ju")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar5(request):
    alumnos = Alumnos.objects.filter(matricula__regex="UTM")
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar6(request):
    alumnos = Alumnos.objects.filter(nombre__in=["Juan", "Ana"])
    return render(request, "registros/consultas.html", {'alumnos': alumnos})

def consultar7(request):
    fechaInicio = datetime.date(2022, 7, 1)
    fechaFin = datetime.date(2022, 7, 13)
    alumnos=Alumnos.objects.filter(created__range=(fechaInicio,fechaFin))
    return render(request,"registros/consultas.html",{'alumnos':alumnos})

def consultar8(request):
    #Consultando entre modelos
    alumnos=Alumnos.objects.filter(comentario__coment__contains='No inscrito')
    return render(request,"registros/consultas.html",{'alumnos':alumnos})



def comentariosFechaORM(request):
    comentarios = ComentarioContacto.objects.filter(
        created__date__range=(
            date(2026, 6, 20),
            date(2026, 8, 5)))
    return render(request,"registros/consultar_comentarios.html",{"comentarios": comentarios})


def comentariosExpresionORM(request):
    comentarios = ComentarioContacto.objects.filter(mensaje__icontains="trabajo")
    return render( request, "registros/consultar_comentarios.html", {"comentarios": comentarios})


def comentariosUsuarioORM(request):
    comentarios = ComentarioContacto.objects.filter(usuario__iexact="Renata")
    return render(request,"registros/consultar_comentarios.html",{"comentarios": comentarios})


def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request, "registros/archivos.html")
        else:
            messages.error(request, "Error al procesar el formulario")
    else:
        return render(request, "registros/archivos.html", {'archivo': Archivos})