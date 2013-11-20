# Create your views here.
from django.http import HttpResponseRedirect

def home(request):
    return HttpResponseRedirect('/produk')
    
def hari_ini(request):
    return HttpResponseRedirect('/produk')
