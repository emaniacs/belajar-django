# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from products.models import Items

def _get_args(request):
    return {
        'MENU': 'pembayaran',
        'user': request.user,
    }
    
def home(request):
    args = _get_args(request)
    
    pembayaran = Items.objects.filter(tipe_item__nama='pembayaran')
    args.update({'pembayaran':pembayaran})
    
    return render_to_response('pembayaran/home.html', args)
    
def bayar(request, tipe):
    args = _get_args(request)
    user = request.user
    
    if user.is_authenticated():
        try:
            ret = render_to_response('pembayaran/%s.html'%tipe, args)
        except:
            args.update({'tipe':tipe})
            ret = render_to_response('pembayaran/unknown_type.html', args)
    else:
        ret = render_to_response('pembayaran/need_login.html', args)
    
    return ret
