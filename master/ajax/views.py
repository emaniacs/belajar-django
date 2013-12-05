from django.shortcuts import render
from products.models import Pelanggan
from django.http import HttpResponseRedirect, HttpResponse
from json import dumps as json_dumps
from django.core import serializers

# Create your views here.

def pelanggan(request):
    data = {
        'status': False,
        'message': 'Invalid data post.',
    }
    
    if request.method == 'POST' and request.is_ajax():
        np = request.POST.get('nama', False)
        if np:
            pel = Pelanggan.objects.filter(nama__contains=np)
            if len(pel) > 0:
                pelanggan = [m['fields'] for m in serializers.serialize('python', pel, fields=('nama', 'no_rek', 'no_hape'))]
                data.update({'data':pelanggan})
                data['status'] = True
    
        ret = HttpResponse(json_dumps(data), content_type='application/json')      
    else:
        ret = HttpResponseRedirect('/')
        
    return ret
