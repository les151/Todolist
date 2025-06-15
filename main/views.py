from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Task
# Create your views here.
def index(request):
    return render(request, 'main.html')

def To_Do_List_page(request):
    user = request.user
    todo_tasks     = Task.objects.filter(user=user, status='todo').order_by('due_date')
    done_tasks     = Task.objects.filter(user=user, status='done').order_by('due_date')
    not_done_tasks = Task.objects.filter(user=user, status='notdone').order_by('due_date')
    return render(request, 'To_Do_List.html', {
        'todo_tasks': todo_tasks,
        'done_tasks': done_tasks,
        'not_done_tasks': not_done_tasks,
    })

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

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        due_date = request.POST.get('due_date')
        if title and due_date:
            Task.objects.create(title = title , due_date = due_date, user = request.user)
    return redirect('main:login')