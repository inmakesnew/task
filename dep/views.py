from django.shortcuts import render

# Create your views here.
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
#Create your views here
def maths(request):
     return render(request, "maths.html")
def stat(request):
     return render(request,"stat.html")
def commerce(request):
     return render(request,"commerse.html")

def english(request):
     return render(request,"english.html")
def eco(request):
     return render(request,"eco.html")