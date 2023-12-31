
from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader

def saludo(request):
    return HttpResponse("Hola Django - nico")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: <br> {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
    return HttpResponse(documentoDeTexto)

def probando_template(request):

    nombre = "Nicolas"
    apellido = "Machado"
    lista_de_notas = [1,2,3,4,8,3,2]

    diccionario = {"nombre": nombre, "apellido": apellido, "hoy": datetime.datetime.now(), "notas": lista_de_notas}
    mi_html = loader.get_template("template1.html")
    documento = plantilla.render(diccionario)

    return HttpResponse(documento)