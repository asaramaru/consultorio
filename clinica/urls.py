"""clinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from centro import views as views_centro
from consultorio import views as views_consultorio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views_centro.login_view, name='login'),
    path('principal/', views_centro.pag_principal, name='principal'),
    path('logout/', views_centro.logout_view, name='logout'),
    path('registro/', views_centro.registro, name='registro'),
    path('recuperar/', views_centro.recuperar_contraseña, name='contraseña'),
    path('formulario/', views_centro.formulario, name='formulario'),
    path('pacientes/', views_consultorio.pacientes_view, name='lista_pacientes'),
    path('pacientes/crear/', views_consultorio.crear_paciente, name='crear_pacientes'),
    path('grupofamiliar/crear/', views_consultorio.crear_grupo_familiar, name='crear_grupo_familiar'),
    path('medico/crear/', views_consultorio.crear_medico, name='crear_medico'),
    path('registro/crear/', views_consultorio.crear_registro, name='crear_registro'),
    path('laboratorio/crear/', views_consultorio.crear_laboratorio, name='crear_laboratorio'),
    path('examen/crear/', views_consultorio.crear_examen, name='crear_examen'),
    path('especialista/cita/', views_consultorio.cita_especilista, name='cita_especialista'),
    path('cita/crear/', views_consultorio.crear_cita, name='crear_cita'),
    path('historiaclinica/crear/', views_consultorio.crear_historia_clinica, name='crear_historia_clinica'),
]
