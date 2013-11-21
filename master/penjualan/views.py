# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from products.models import Penjualan
from django.utils import timezone
from django.db.models import Sum

import datetime

def home(request):
    return HttpResponseRedirect('/penjualan/hari-ini')
    
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
        
    args.update({'sekarang': sekarang})
    args.update({'penjualan': penjualan})
    args.update({'uang': penjualan.aggregate(Sum('harga_total'))})
    args.update({'total_penjualan': len(penjualan)})
    
    return render_to_response(view, args)

def by_filter(request, tahun, bulan=None, hari=None):
    user = request.user
    
    if not user.is_superuser:
        return HttpResponseRedirect('/penjualan/')
        
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
        
    penjualan = Penjualan.objects.filter(waktu_beli__range=[waktu, waktu_range])
    
    view = 'penjualan/hari_ini.html'
    args = {}
    args.update({'user': user})
    args.update({'penjualan': penjualan})
    args.update({'total_uang': penjualan.aggregate(Sum('harga_total'))})
    args.update({'total_penjualan': len(penjualan)})
    
    return render_to_response(view, args)
    
def by_range(request, t1, b1, h1, t2, b2, h2):
    user = request.user
    
    if not user.is_superuser:
        return HttpResponseRedirect('/penjualan/')
        
    waktu1 = datetime.date(int(t1), int(b1), int(h1))
    waktu2 = datetime.date(int(t2), int(b2), int(h2))
    
    view = 'penjualan/by_range.html'
    
    args = {}
    args.update({'user': user})
    
    penjualan = Penjualan.objects.filter(waktu_beli__range=[waktu1, waktu2])
    
    args.update({'penjualan': penjualan})
    args.update({'total_uang': penjualan.aggregate(Sum('harga_total'))})
    args.update({'penjualan': len(penjualan)})
    
    return render_to_response(view, args)

    

def semua(request):
    user = request.user
    if not user.is_superuser:
        return HttpResponseRedirect('/produk')
        
    
