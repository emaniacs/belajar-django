from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ItemType(models.Model):
    nama = models.CharField(max_length=32)
    nama_keren = models.CharField(max_length=32)
    waktu_input = models.DateTimeField('date adding', default=timezone.now)
    
    def __unicode__(self):
        return self.nama_keren.capitalize()
    
    class Meta:
        verbose_name_plural = 'Jenis item'
    

class Items(models.Model):
    nama = models.CharField(max_length=64)
    waktu_input = models.DateTimeField('date adding')
    waktu_modif = models.DateTimeField('date modified')
    tipe_item = models.ForeignKey(ItemType)
    user = models.ForeignKey(User)
    harga_beli = models.IntegerField()
    harga_jual = models.IntegerField()
    harga_minimal = models.IntegerField()
    stok = models.IntegerField(default=0)
    img = models.CharField(max_length=64,default='/static/img/empty.png')
    status = models.IntegerField(default=1)
    
    def __unicode__(self):
        return '(%s) - %s' % (self.tipe_item.nama_keren, self.nama)
        
    class Meta:
        verbose_name_plural = 'Daftar Item'

class Pelanggan(models.Model):
    nama = models.CharField(max_length=64)
    alamat = models.TextField(default='')
    no_hape = models.CharField(max_length=16)

class Penjualan(models.Model):
    nama = models.CharField(max_length=64)
    waktu_beli = models.DateTimeField('purchase date')
    harga = models.IntegerField()
    jumlah = models.IntegerField()
    user = models.ForeignKey(User)
    harga_total = models.IntegerField()
    pelanggan = models.ForeignKey(Pelanggan)
    kode = models.CharField(max_length=32)
    dll = models.CharField(max_length=32)
    
class Log(models.Model):
    nama = models.CharField(max_length=64)
    waktu_input = models.DateTimeField('add date')
    user = models.ForeignKey(User)
    data = models.TextField()
    
    
