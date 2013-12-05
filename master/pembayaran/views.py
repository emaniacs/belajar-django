# Create your views here.
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from products.models import Items, Menu
from django.core.context_processors import csrf

def _get_args(request):
    return {
        'MENU': 'pembayaran',
        'user': request.user,
    }

def _is_active():
    try:
        menu = Menu.objects.get(key='pembayaran')
        
        if menu.status != 1:
            raise Http404
    except:
        raise Http404    
    
def home(request):
    _is_active()
    
    args = _get_args(request)
    
    pembayaran = Items.objects.filter(tipe_item__nama='pembayaran')
    args.update({'pembayaran':pembayaran})
    
    return render_to_response('pembayaran/home.html', args)
    
def bayar(request, tipe):
    _is_active()
    
    args = _get_args(request)
    args.update(csrf(request))
    user = request.user
    
    if user.is_authenticated():
        try:
            ret = render_to_response('pembayaran/%s.html' % tipe.lower(), args)
        except:
            args.update({'tipe':tipe})
            ret = render_to_response('pembayaran/unknown_type.html', args)
    else:
        ret = HttpResponseRedirect('/login')
    
    return ret

def bayar_save(request, tipe):
    _is_active()
        
    return bayar(request, tipe)
