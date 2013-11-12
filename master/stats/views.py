from django.shortcuts import render_to_response
from django.http import HttpResponseForbidden

def home(request):
    if not request.user.is_superuser:
        return HttpResponseForbidden()
    
    args = {}
    
    return render_to_response('page/home.html', args)
