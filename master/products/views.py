# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from products.models import Items, ItemType, Penjualan, Pelanggan
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from json import dumps as json_dumps

from master.utils import random_string

def _get_args(request, tipe):
    return {
        'MENU': tipe,
        'user': request.user,
    }
    
def home(request):
    args = _get_args(request, 'produk')
    
    view = 'products/home.html'
    tipe = ItemType.objects.exclude(nama='pembayaran')
    args.update({'all_type': tipe})
    args.update({'login_error': request.session.get('login_error')})
    
    try:
        del request.session['login_error']
    except:
        pass
    
    return render_to_response(view, args)
    
# TODO(print)
def beli(request):
    data = {}
    user = request.user
    if request.method == 'POST' and request.is_ajax():
        if user.is_authenticated():
            item_id = _p(request, 'id')
            harga = _p(request, 'harga', False)
            jumlah = _p(request, 'jumlah', False)
            dll = _p(request, 'dll', '')
            nama_pelanggan = _p(request, 'nama_pelanggan', False)
            pembayaran = _p(request, 'pembayaran', 'lunas')
            user = request.user
            
            if item_id and harga and jumlah and nama_pelanggan:
                try:
                    item = Items.objects.get(id=item_id)
                    
                    try:
                        pelanggan = Pelanggan.objects.get(nama=nama_pelanggan)
                    except:
                        pelanggan = Pelanggan(nama=nama_pelanggan)
                        pelanggan.save()
                        
                    jumlah = int(jumlah)
                    if jumlah <= item.stok :
                        penjualan = Penjualan(item=item, user=user, waktu_beli=timezone.now())
                        penjualan.harga = int(harga)
                        penjualan.jumlah = jumlah
                        penjualan.harga_total = int(harga) * int(jumlah)
                        penjualan.kode = random_string(8)
                        penjualan.pelanggan = pelanggan
                        penjualan.pembayaran = pembayaran
                        penjualan.dll = dll
                        penjualan.save()
                        item.stok -= jumlah
                        item.save()
                        data.update({
                            'code'  : penjualan.kode,
                            'status': True,
                            'stock' : item.stok,
                            'message': 'Ok'
                        })
                    else:
                        data.update({
                            'status': False,
                            'message': 'Out of stock'
                        })
                except Items.DoesNotExist:
                    data.update({
                        'status': False,
                        'message': 'Item did not exist'
                    })
                except Exception, e:
                    data.update({
                        'status': False,
                        'message': 'Unknown error' + str(e)
                    })
            else:
                data.update({
                    'status': False,
                    'message': 'Invalid data post'
                })
        else:
            data.update({
                'status': False,
                'message': 'Login expired, please relogin.'
            })
    else:
        return HttpResponseRedirect('/produk/')
    
    return HttpResponse(json_dumps(data), content_type='application/json')

def by_type(request, item_type):
    args = _get_args(request, item_type.lower())
    view = 'products/by_type.html'

    all_items = Items.objects.count()
    args.update({'all_items': all_items})
    args.update({'item_type': item_type})
    
    return render_to_response(view, args)
    
def by_type_detail(request, item_type, item_id, item_name=None):
    view = 'products/detail.html'
    args = _get_args(request, item_type.lower())
    try:
        items = Items.objects.get(id=item_id, tipe_item__nama=item_type)
        args.update({'items': items})
    except Items.DoesNotExist:
        view = 'products/notfound.html'
    except:
        raise
    
    return render_to_response(view, args)

def _tmp(request):
    data = request.session.get('data_checkout')
    return HttpResponse(json_dumps(data), content_type='application/json')

def add(request):
    item_id = _p(request, 'id', False)
    jumlah = _p(request, 'jumlah', False)
    data = {}
    if request.method == 'POST' and request.is_ajax():
        if item_id and jumlah:
            try:
                item = Items.objects.get(id=item_id)
                data_checkout = request.session.get('data_checkout', {})
                
                if data_checkout.has_key(item_id):
                    tmp = data_checkout[item_id]
                    jumlah = str(int(tmp) + int(jumlah))
                    data_checkout[item_id] = jumlah
                else:
                    data_checkout.update({item.id: jumlah})
                
                request.session['data_checkout'] = data_checkout
                data.update({
                    'status': True,
                    'message': 'Ok',
                    'data': {item_id:jumlah}
                })
            except Items.DoesNotExist:
                data.update({
                    'status' : False,
                    'message': 'Unknown error (%s ' % str(e)
                })
        else:
            data.update({
                'status' : False,
                'message' : 'Invalid data post'
            })
        
    else:
        return HttpResponseRedirect('/produk/')
    
    return HttpResponse(json_dumps(data), content_type='application/json')
    
def checkout(request):
    pass


def _p(request, name, default=None):
    return request.POST.get(name, default)
