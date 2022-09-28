from http.client import HTTPResponse
from datetime import datetime
from django.http import HttpResponse
from django.template import Context, Template

def hola(request):
    return HttpResponse('<h1>Buenos Dias</h1>')

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f'Fecha y Hora Actual es {fecha_actual}')

def fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f'Según tu edad {edad} tu año de nacimeinto es {fecha}')

def mi_template(request):
    carga_file = open(r'C:\Trabajo\TrabajoConPython\PROYECTO-CLASES\proyectoClase\templates\template.html', 'r')
    template = Template(carga_file.read())
    carga_file.close()
    contexto = Context()
    render_template = template.render(contexto)
    return HttpResponse(render_template)