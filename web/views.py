from django.shortcuts import render, redirect
# importamos la clase View
from django.views import View
from .models import *
from .forms import *

# Create your views here.
class AlumnoView(View):
    def get(self,request):
        listaAlumnos = TblAlumno.objects.all()
        formAlumno = AlumnoForm()
        context = {
        'alumnos' : listaAlumnos,
        'formAlumno': formAlumno
        }
        return render(request,'index.html',context)
    def post(self, request):
        formAlumno = AlumnoForm(request.POST)
        if formAlumno.is_valid():
            formAlumno.save()
        return redirect('/')
  
def deleteAlumno(request , pk):
    print(str(pk)+"ddddddddddddd======================")
    alumno = TblAlumno.objects.filter(alumno_id = pk)
    alumno.delete()
    return redirect('/')


#PROFESOR
class ProfesorView(View):
    def get(self,request):
        listaProfesores = TblProfesor.objects.all()
        formProfesor = ProfesorForm()
        context = {
        'profesores' : listaProfesores,
        'formProfesor': formProfesor
        }
        return render(request,'index_profesor.html',context)
    def post(self, request):
        formProfesor = ProfesorForm(request.POST)
        if formProfesor.is_valid():
            formProfesor.save()
        return redirect('/profesores')
  
def deleteProfesor(request , pk):

    profesor = TblProfesor.objects.filter(profesor_id = pk)
    profesor.delete()
    return redirect('/profesores')