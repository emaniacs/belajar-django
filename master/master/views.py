from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib.auth import logout, login, authenticate
from django.core.context_processors import csrf

def home(request):
    return HttpResponseRedirect('/produk')

def llogin(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/produk')
        
    ret = None
    args = {}
    if request.method == 'POST':
        username = request.POST['u']
        password = request.POST['p']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                try:
                    del request.session['login_error']
                except:
                    pass
                login(request, user)
                ret = HttpResponseRedirect('/produk')
            else:
                request.session['login_error'] = 'Maaf user anda tidak aktif'
                ret = HttpResponseRedirect('/produk')
        else:
            args.update(csrf(request))
            args.update({'login_error': 'Login gagal.'})
            args.update({'username': username})
            ret = render_to_response('page/login_form.html', args)
    else:
        args.update(csrf(request))
        ret = render_to_response('page/login_form.html', args)
        
    return ret
    
def llogout(request):
    logout(request);
    return HttpResponseRedirect('/produk')

def error404(request):
    return render_to_response('404.html')

