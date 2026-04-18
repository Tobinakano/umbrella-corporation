from django.shortcuts import render

def index_view(request):
	quick_error = None
	quick_success = None
	if request.method == 'POST' and request.path == '/quick_register/':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if not username or not password:
			quick_error = 'Debes ingresar usuario y contraseña.'
		elif quick_user_exists(username):
			quick_error = 'El usuario ya existe.'
		else:
			with open('quick_users.txt', 'a', encoding='utf-8') as f:
				f.write(f'{username}:{password}\n')
			quick_success = 'Usuario registrado correctamente.'
	return render(request, 'index.html', {'quick_error': quick_error, 'quick_success': quick_success})

def quick_user_exists(username):
	import os
	if not os.path.exists('quick_users.txt'):
		return False
	with open('quick_users.txt', 'r', encoding='utf-8') as f:
		for line in f:
			user, _ = line.strip().split(':')
			if user == username:
				return True
	return False

def empresa_view(request):
	return render(request, 'empresa.html')

def investigacion_view(request):
	return render(request, 'investigacion.html')

def ubicaciones_view(request):
	return render(request, 'ubicaciones.html')
