from django.shortcuts import render_to_response
from products.models import Items

def home(request):
    args = {}
    pulsa = Items.objects.filter(tipe_item__nama='pulsa').order_by('-waktu_modif')[:4]
    args['all_pulsa'] = pulsa
    args['total_pulsa'] = len(Items.objects.filter(tipe_item__nama='pulsa'))
    
    return render_to_response('page/home.html', args)

def error404(request):
    return render_to_response('404.html')
