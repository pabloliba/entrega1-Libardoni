from django.shortcuts import render
from django.template import Template, loader, Context
from django.http import HttpResponse
from appcoder.forms import *
# Create your views here.
 
def inicio (request):
   return render(request,'inicio.html')  

def autos (request):
   return render(request,'autos.html')  

def motos (request):
   return render(request,'motos.html')  

def empleados (request):
    if request.method=='POST':
          form=formempleado(request.POST)
          if form.is_valid:
            informacion=form.cleaned_data
            nombre=informacion[nombre]
            documento=informacion[documento]
            empleado=empleado(nombre=nombre,documento=documento)
            empleado.save()
            return render(request, 'appcoder/empleados.html',{'empleado guardado correctamente'})
      
    else:
      formulario=formempleado()
      return render(request,'empleados.html',{"form":formulario}) 