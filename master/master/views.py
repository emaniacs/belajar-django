from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect

def home(request):
    return HttpResponseRedirect('/produk')

def error404(request):
    return render_to_response('404.html')
