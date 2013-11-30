# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def home(request):
    args = {
        'user': request.user,
        'MENU': 'pembayaran'
    }
    return render_to_response('pembayaran/home.html', args)
    
def bayar(request, tipe):
    args = {}
    user = request.user
    args.update({'user':user})
    
    if user.is_authenticated():
        try:
            ret = render_to_response('pembayaran/%s.html'%tipe, args)
        except:
            args.update({'tipe':tipe})
            ret = render_to_response('pembayaran/unknown_type.html', args)
    else:
        ret = render_to_response('pembayaran/need_login.html', args)
    
    return ret
