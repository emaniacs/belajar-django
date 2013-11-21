# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from products.models import Penjualan
from django.utils import timezone

import datetime

def home(request):
    return HttpResponseRedirect('/produk')
    
def hari_ini(request):
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect('/produk')
        
    view = 'penjualan/hari_ini.html'
    args = {}
    args.update({'user': user})
    
    sekarang = datetime.date.today()
    
    if user.is_superuser:
        penjualan = Penjualan.objects.filter(waktu_beli__gt=sekarang)
    else:
        penjualan = Penjualan.objects.filter(waktu_beli__gt=sekarang, user=request.user)
        
    args.update({'penjualan': penjualan})
    
    return render_to_response(view, args)

def by_filter(request, tahun, bulan=None, hari=None):
    user = request.user
    tahun = int(tahun)
    
    if hari is not None:
        hari = int(hari)
        bulan = int(bulan)
        waktu_range = datetime.date(tahun, bulan, hari+1)
    elif bulan is not None:
        hari = 1
        bulan = int(bulan)
        waktu_range = datetime.date(tahun, bulan+1, 1)
    else:
        hari = 1
        bulan = 1
        waktu_range = datetime.date(int(tahun)+1, 1, 1)
        
    waktu = datetime.date(tahun, bulan, hari)
        
    
    view = 'penjualan/hari_ini.html'
    args = {}
    args.update({'user': user})
    #~ args.update({'satu': waktu})
    #~ args.update({'dua': waktu_range})
    
    penjualan = Penjualan.objects.filter(waktu_beli__range=[waktu, waktu_range])
    
    args.update({'penjualan': penjualan})
    
    return render_to_response(view, args)
    

def semua(request):
    user = request.user
    if not user.is_superuser:
        return HttpResponseRedirect('/produk')
        
    
