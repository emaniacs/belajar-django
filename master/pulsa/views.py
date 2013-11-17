# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from products.models import Items, ItemType
from django.core.context_processors import csrf

NAME = 'pulsa'
def home(request):
    view = 'pulsa/home.html'
    args = _get_args()
    
    args.update({'all_pulsa': Items.objects.filter(tipe_item__nama=NAME)})
    args.update({'title': 'HomePage'})
    
    return render_to_response(view, args)

def detail(request, pulsa_id=None):
    view = 'pulsa/detail.html'
    args = _get_args()
    
    pulsa = get_object_or_404(Items, id=pulsa_id)
    args.update({'pulsa':pulsa})
    
    return render_to_response(view, args)
    
def beli(request, pulsa_id=None):
    view = 'pulsa/beli_form.html'
    args = {}
    args = _get_args()
    
    pulsa = get_object_or_404(Items, id=pulsa_id)    
    
    if request.method == 'POST':
        jumlah = request.POST.get('jumlah', 0)
    else:
        args.update({'pulsa':pulsa})
        args.update(csrf(request))
    
    return render_to_response(view, args)

def _get_args():
    args = {}
    args.update({'MENU': NAME})
    return args
