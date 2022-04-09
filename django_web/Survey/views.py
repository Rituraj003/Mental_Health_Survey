
from django.shortcuts import render
import pickle

# Create your views here.

def home(request):
    return render(request,'index.html')