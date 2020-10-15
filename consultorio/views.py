from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from consultorio.models import Paciente, GrupoFamiliar, Medico, Registro, Laboratorio, Cita, Especialista, Examen, HistoriaClinica, CitaEspecialista

# Create your views here.

@login_required
def pacientes_view(request):
	if request.GET['cedula']:
		filtro = request.GET['cedula']
		if len(filtro)>11:
			error = {'error':'la busqueda esta muy largo'}
		else:
			paciente = Paciente.objects.filter(name__icontains=filtro)
			return render(request,'resultados.html',{'paciente':paciente,'query':filtro})
	#lista = Paciente.objects.all().order_by('modified')
	return render(request,'resultados.html',{'lista':lista,'error':error})

@login_required
def crear_medico(request):
	if request.method == 'POST':
		medico = Medico()
		nombre = request.POST['nombre']
		apellido = request.POST['apellido']
		cedula = request.POST['cedula']
		correo = request.POST['correo']
		tipoSangre = request.POST['tipoSangre']
		telefono = request.POST['telefono']
		celular = request.POST['celular']
		fechaNacimiento = request.POST['fechaNacimiento']

		medico = Medico.objects.create(Nombre=nombre
			,Apellido=apellido
			,Cedula=cedula
			,Correo=correo
			,TipoSangre=tipoSangre
			,Telefono=telefono
			,Celular=celular
			,FechaNacimiento=fechaNacimiento)

		return redirect('crear_medico')

	return render(request,'crear_medico.html')

@login_required
def crear_grupo_familiar(request):
	if request.method == 'POST':
		nombre = request.POST['nombre']
		titular = request.POST['titular']
		idMedico = request.POST['idMedico']

		grupofamiliar = GrupoFamiliar.objects.create(Nombre=nombre,Titular=titular,IdMedico=idMedico)

		return redirect('crear_grupo_familiar')
	medico = Medico.objects.all()
	return render(request,'crear_grupo_familiar.html',{'medico':medico})

@login_required
def crear_paciente(request):
	if request.method == 'POST':
		nombre = request.POST['nombre']
		apellido = request.POST['apellido']
		cedula = request.POST['cedula']
		correo = request.POST['correo']
		tipoSangre = request.POST['tipoSangre']
		telefono = request.POST['telefono']
		celular = request.POST['celular']
		fechaNacimiento = request.POST['fechaNacimiento']
		estrato = request.POST['estrato']
		idGrupoFamiliar = request.POST['idGrupoFamiliar']
		

		paciente = Paciente.objects.create_user(Nombre= nombre
			,Apellido= apellido
			,Cedula= cedula
			,Correo= correo
			,TipoSangre= tipoSangre
			,Telefono= telefono
			,Celular= celular
			,FechaNacimiento= fechaNacimiento
			,Estrato= estrato
			,IdGrupoFamiliar= idGrupoFamiliar)

		return redirect('crear_pacientes')

	grupofamiliar = GrupoFamiliar()
	print(grupofamiliar)
	return render(request,'crear_paciente.html',{'grupo':grupofamiliar})

@login_required
def crear_registro(request):
	if request.method == 'POST':
		sintomas = request.POST['sintomas']
		medicamentos = request.POST['medicamentos']
		signosvitales = request.POST['signosvitales']
		generacion = request.POST['generacion']
		incapacidades = request.POST['incapacidades']
		remisiones = request.POST['remisiones']
		ordenesmedicas = request.POST['ordenesmedicas']


		registro = Registro.objects.create(Sintomas= sintomas
				,Medicamentos= medicamentos
				,SignosVitales= signosvitales
				,Generacion= generacion
				,Incapacidades= incapacidades
				,Remisiones= remisiones
				,OrdenesMedicas= ordenesmedicas)

		return redirect('crear_registro')
	return render(request,'crear_registro.html')

@login_required
def crear_laboratorio(request):
	if request.method == 'POST':
		nombre = request.POST['nombre']
		cede = request.POST['cede']
		direccion = request.POST['direccion']
		horario = request.POST['horario']

		laboratorio = Laboratorio.objects.create(Nombre= nombre
				,Sede= cede
				,Direccion= direccion
				,Horario= horario)

		return redirect('crear_laboratorio')
	return render(request,'crear_laboratorio.html')

@login_required
def crear_examen(request):
	if request.method == 'POST':
		resultados = request.POST['resultados']
		fecha = request.POST['fecha']
		laboratorio = request.POST['idLaboratorio']
		paciente = request.POST['idPaciente']

		examen = Examen.objects.create(Resultados= resultados
			,FechaExamen= fecha
			,IdLaboratorio= laboratorio
			,IdPaciente= paciente)

		return redirect('crear_examen')
	return render(request,'crear_examen.html')

@login_required
def cita_especilista(request):
	if request.method == 'POST':
		fechaCita = request.POST['fechaCita']
		tipoCita = request.POST['tipoCita']
		observaciones = request.POST['observaciones']
		idPaciente = request.POST['idPaciente']
		idEspecialista = request.POST['idEspecialista']
		idRegistro = request.POST['idRegistro']

		citaEspecialista = CitaEspecialista.objects.create(FechaCita= fechaCita
			,TipoCita= tipoCita
			,Observaciones= observaciones
			,IdPaciente= idPaciente
			,IdEspecialista= idEspecialista
			,IdRegistro= idRegistro)

		return redirect('cita_especilista')
	return render(request,'cita_especilista.html')

@login_required
def crear_especialista(request):
	if request.method == 'POST':
		nombre = request.POST['nombre']
		apellido = request.POST['apellido']
		cedula = request.POST['cedula']
		correo = request.POST['correo']
		tipoSangre = request.POST['tipoSangre']
		telefono = request.POST['telefono']
		celular = request.POST['celular']
		fechaNacimiento = request.POST['fechaNacimiento']
		especialidad = request.POST['especialidad']
		

		especialista = Especialista.objects.create_user(Nombre= nombre
			,Apellido= apellido
			,Cedula= cedula
			,Correo= correo
			,TipoSangre= tipoSangre
			,Telefono= telefono
			,Celular= celular
			,FechaNacimiento= fechaNacimiento
			,Especialidad= especialidad)

		return redirect('crear_especialista')
	return render(request,'crear_especialista.html')

@login_required
def crear_cita(request):
	if request.method == 'POST':
		idPaciente = request.POST['idPaciente']
		idMedico = request.POST['idMedico']
		idRegistro = request.POST['idRegistro']
		fechaCita = request.POST['fechaCita']
		tipoCita = request.POST['tipoCita']
		observaciones = request.POST['observaciones']

		cita = Cita.objects.create(IdPaciente= idPaciente
			,IdMedico= idMedico
			,IdRegistro= idRegistro
			,FechaCita= fechaCita
			,TipoCita= tipoCita
			,Observaciones= observaciones)

		return redirect('crear_cita')
	return render(request,'crear_cita.html')

@login_required
def crear_historia_clinica(request):
	if request.method == 'POST':
		idPaciente = request.POST['idPaciente']
		idCita = request.POST['idCita']
		idExamen = request.POST['idExamen']

		historiaClinica = HistoriaClinica.objects.create(IdPaciente= idPaciente
			,IdCita= idCita
			,IdExamen= idExamen)

		return redirect('crear_historia_clinica')
	paciente = Paciente.objects.all()
	cita = Cita.objects.all()
	examen = Examen.objects.all()
	return render(request,'crear_historia_clinica.html',{'paciente':paciente,'cita':cita,'examen':examen})