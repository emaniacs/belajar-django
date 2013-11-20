# Create your views here.
from django.http import HttpResponseRedirect

def home(request):
    return HttpResponseRedirect('/produk')
    
def bayar(request, tipe):
    return HttpResponseRedirect('/produk')
