from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def pacientes_view(request):
	search_fields=('username')
	lista = Pacientes.objects.all().order_by('modified')
	return render(request,'base.html',{'lista':lista})

@login_required
def crear_paciente(request):
	pass