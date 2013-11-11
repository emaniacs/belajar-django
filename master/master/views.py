from django.shortcuts import render_to_response
from products.models import Items

def home(request):
    args = {}
    pulsa = Items.objects.filter(item_type__name='pulsa').order_by('-mod_date')[:4]
    args['all_pulsa'] = pulsa
    args['total_pulsa'] = len(Items.objects.filter(item_type__name='pulsa'))
    
    return render_to_response('page/home.html', args)

def error404(request):
    return render_to_response('404.html')
