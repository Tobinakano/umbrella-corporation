from django.shortcuts import render, redirect
from django.http import HttpResponse
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USERS_FILE = os.path.join(BASE_DIR, 'users.txt')

def login_view(request):
	error = None
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if authenticate_user(username, password):
			return render(request, 'login_success.html', {'username': username})
		else:
			error = 'Usuario o contraseña incorrectos.'
	return render(request, 'login.html', {'error': error})

def authenticate_user(username, password):
	if not os.path.exists(USERS_FILE):
		return False
	with open(USERS_FILE, 'r', encoding='utf-8') as f:
		for line in f:
			user, pwd = line.strip().split(':')
			if user == username and pwd == password:
				return True
	return False

def register_view(request):
	error = None
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if user_exists(username):
			error = 'El usuario ya existe.'
		else:
			with open(USERS_FILE, 'a', encoding='utf-8') as f:
				f.write(f'{username}:{password}\n')
			return redirect('login')
	return render(request, 'register.html', {'error': error})

def user_exists(username):
	if not os.path.exists(USERS_FILE):
		return False
	with open(USERS_FILE, 'r', encoding='utf-8') as f:
		for line in f:
			user, _ = line.strip().split(':')
			if user == username:
				return True
	return False
