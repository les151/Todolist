from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request, 'main.html')

def To_Do_List_page(request):
    return render(request, 'To_Do_List.html')

def sign_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']


        user = authenticate(request, username = username, password = password)

        if user:
            login(request, user)
            return redirect('main:login')
    
    return render(request, 'sign_in.html') 

def sign_up(request):
    if request.method == "POST":
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:sign_in')
    else:
        form = UserCreationForm()
    
    return render(request, 'sign_up.html')