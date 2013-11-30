# Create your views here.
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from products.models import Penjualan
from django.utils import timezone
from django.db.models import Sum

import datetime

def _get_args(request):
    return {
        'MENU': 'penjualan',
        'user': request.user,
    }

def home(request):
    args = _get_args(request)
    return HttpResponseRedirect('/penjualan/hari-ini', args)
    
def hari_ini(request):
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect('/produk')
        
    view = 'penjualan/hari_ini.html'
    
    args = _get_args(request)
    
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
        
    tahun = 1 if int(tahun) < 1 else int(tahun)
    if hari is not None:
        hari = 1 if int(hari) < 1 else int(hari)
        bulan = int(bulan)
        waktu_range = datetime.date(tahun, bulan, hari+1)
    elif bulan is not None:
        hari = 1
        bulan = 1 if int(bulan) < 1 else int(bulan)
        waktu_range = datetime.date(tahun, bulan+1, 1)
    else:
        hari = 1
        bulan = 1
        waktu_range = datetime.date(tahun+1, 1, 1)
        
    waktu = datetime.date(tahun, bulan, hari)
        
    penjualan = Penjualan.objects.filter(waktu_beli__range=[waktu, waktu_range])
    
    view = 'penjualan/hari_ini.html'
    
    args = _get_args(request)
    args.update({'sekarang': waktu})
    args.update({'waktu_range': waktu_range})
    args.update({'penjualan': penjualan})
    args.update({'uang': penjualan.aggregate(Sum('harga_total'))})
    args.update({'total_penjualan': len(penjualan)})
    
    return render_to_response(view, args)
    
def by_range(request, t1, b1, h1, t2, b2, h2):
    user = request.user
    
    if not user.is_superuser:
        return HttpResponseRedirect('/penjualan/')

    t1 = 1 if int(t1) < 1 else int(t1)
    b1 = 1 if int(b1) < 1 else int(b1)
    h1 = 1 if int(h1) < 1 else int(h1)
    t2 = 1 if int(t2) < 1 else int(t2)
    b2 = 1 if int(b2) < 1 else int(b2)
    h2 = 1 if int(h2) < 1 else int(h2)
        
    waktu1 = datetime.date(t1, b1, h1)
    waktu2 = datetime.date(t2, b2, h2+1)
    
    view = 'penjualan/by_range.html'
    
    
    args = _get_args(request)
    
    penjualan = Penjualan.objects.filter(waktu_beli__range=[waktu1, waktu2])
    
    
    waktu2 = datetime.date(t2, b2, h2)
    args.update({'penjualan': penjualan})
    args.update({'waktu1': waktu1})
    args.update({'waktu2': waktu2})
    args.update({'uang': penjualan.aggregate(Sum('harga_total'))})
    args.update({'total_penjualan': len(penjualan)})
    
    return render_to_response(view, args)

    

def semua(request):
    user = request.user
    if not user.is_superuser:
        return HttpResponseRedirect('/produk')
        
    
