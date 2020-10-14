from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
def pag_principal(request):
	return render(request,'base.html')

def formulario(request):
	if request.method == 'POST':
		nombre = request.POST['nombre']
		mensaje = request.POST['mensaje']
		email = request.POST['email']

		if nombre and mensaje and email:
			send_mail(nombre,mensaje,email,['suppordani@gmail.com'])
		else:
			return render(request,'formulario.html',{'error':'Se te ha olvidado llenar un campo'})

	return render(request,'formulario.html')

def login_view(request):
	if request.method == 'POST':
		usuario = request.POST['usuario']
		contraseña = request.POST['password']

		user = authenticate(request,username=usuario, password=contraseña)

		if user is not None:
			login(request, user)
			return redirect('principal')
		else:
			return render(request,'login.html',{'error':'Usuario y/o contraseña incorrecto'})
	return render(request,'login.html')

def registro(request):
	if request.method == 'POST':
		usuario = request.POST['usuario']
		password = request.POST['password']
		password_confirmation = request.POST['password_confirmation']

		nombre = request.POST['nombre']
		apellido = request.POST['apellido']
		email = request.POST['email']

		user = User.objects.create_user(username=usuario, password=password, first_name=nombre, last_name=apellido, email=email)
		user.is_admin=False
		user.save()
		return redirect('login')

	return render(request,'registro.html',{'error':'las constraseñas no coinciden'})

def recuperar_contraseña(request):
	if request.method == 'POST':
		usuario = request.POST['usuario']
		password_nueva = request.POST['password_nueva']
		user = User.objects.get(username=usuario)
		user.set_password(password_nueva)
		user.save()
		return redirect('login')

	return render(request, 'recuperar.html',{'error':'El usuario no existe'})

def logout_view(request):
	logout(request)
	return redirect('login')