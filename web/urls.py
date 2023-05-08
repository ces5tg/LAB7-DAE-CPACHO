from django.urls import path

from . import views

app_name = 'web'

urlpatterns = [
    path('', views.AlumnoView.as_view(),name='index'),
    path('deleteAlumno/<int:pk>', views.deleteAlumno,name='deleteAlumno'),
    path('profesores', views.ProfesorView.as_view(),name='index_profesor'),
    path('deleteProfesor/<int:pk>', views.deleteProfesor,name='deleteProfesor')
]