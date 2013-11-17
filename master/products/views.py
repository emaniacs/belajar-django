# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from products.models import Items, ItemType
from django.core.context_processors import csrf

def home(request):
    view = 'products/home.html'
    args = {}
    tipe = ItemType.objects.all()
    args.update({'all_type': tipe})
    args['user'] = request.user
    
    return render_to_response(view, args)
    
def beli(request, item_id=None):
    view = 'pulsa/beli_form.html'
    args = {}
    args = _get_args()
    
    pulsa = get_object_or_404(Items, id=item_id)    
    
    if request.method == 'POST':
        jumlah = request.POST.get('jumlah', 0)
    else:
        args.update({'pulsa':pulsa})
        args.update(csrf(request))
    
    return render_to_response(view, args)
    
def by_type(request, item_type):
    view = 'products/by_type.html'
    args = _get_args(item_type.lower())
    items = Items.objects.filter(tipe_item__nama=item_type)
    args.update({'items': items})
    
    return render_to_response(view, args)
    
def by_type_detail(request, item_type, item_id, item_name=None):
    view = 'products/detail.html'
    args = _get_args(item_type.lower())
    try:
        items = Items.objects.get(id=item_id, tipe_item__nama=item_type)
        args.update({'items': items})
    except Items.DoesNotExist:
        view = 'products/notfound.html'
    except:
        raise
    
    return render_to_response(view, args)

def _get_args(menu=''):
    args = {}
    args.update({'MENU': menu})
    return args
