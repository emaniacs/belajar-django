# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from products.models import Items, ItemType

NAME = 'pulsa'
TYPE = ItemType.objects.get(name=NAME)

def home(request):
    view = 'pulsa/home.html'
    args = {}
    args.update({'all_pulsa': Items.objects.filter(item_type=TYPE)})
    args.update({'title': 'HomePage'})
    
    return render_to_response(view, args)

def detail(request, pulsa_id=None):
    view = 'pulsa/home.html'
    args = {}
    
    obj = get_object_or_404(Items, id=pulsa_id)
    
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
