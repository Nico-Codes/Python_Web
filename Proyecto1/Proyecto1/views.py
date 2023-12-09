from django.http import HttpResponse
import datetime

def saludo(request):
    return HttpResponse("Hola Django - nico")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documentoDeTexto = f"Hoy es dia: <br> {dia}"
    return HttpResponse(documentoDeTexto)

def miNombreEs(self, nombre):
    documentoDeTexto = f"Mi nombre es: <br><br> {nombre}"
    return HttpResponse(documentoDeTexto)
