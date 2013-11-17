# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from products.models import Items, ItemType
from django.core.context_processors import csrf


NAME = ''
def home(request):
    args = {}
    tipe = ItemType.objects.all()
    args.update({'all_type': tipe})
    args['user'] = request.user
    
    return render_to_response('products/home.html', args)
        
def detail(request, item_id=None):
    view = 'pulsa/detail.html'
    args = _get_args()
    
    pulsa = get_object_or_404(Items, id=item_id)
    args.update({'pulsa':pulsa})
    
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
    NAME = item_type.lower()
    return HttpResponseRedirect('/')
    
def by_type_detail(request, item_type, item_id):
    NAME = item_type.lower()
    items = get_object_or_404(Items, id=item_id, tipe_item__nama=item_type)
    args = _get_args()
    
    return render_to_response('/products/detail.html', args)

def _get_args():
    args = {}
    args.update({'MENU': NAME})
    return args
