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
]
