# Create your views here.
from django.shortcuts import render_to_response

def home(request):
    view = 'pulsa/home.html'
    args = {}
    
    return render_to_response(view, args)

def detail(request):
    view = 'pulsa/home.html'
    args = {}
    
    return render_to_response(view, args)
    
def remove(request, pulsa_id=None):
    view = 'pulsa/home.html'
    args = {}
    
    return render_to_response(view, args)
    
def edit(request, pulsa_id=None):
    view = 'pulsa/home.html'
    args = {}
    
    return render_to_response(view, args)
    
def add(request):
    view = 'pulsa/home.html'
    args = {}
    
    return render_to_response(view, args)
