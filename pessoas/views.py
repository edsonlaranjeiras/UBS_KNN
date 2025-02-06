# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

def ver_home(request):
    return render(request, 'ver_avisos.html')