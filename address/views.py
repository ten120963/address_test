from django.shortcuts import render, redirect

def home(request):
	return render(request, 'home.html', {})

def add(request):
	return render(request, 'add.html', {})	

