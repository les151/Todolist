from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, 'main.html')

def sign_in_page(request):
    return render(request, 'sign_in.html')