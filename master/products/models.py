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
    no_hape = models.CharField(max_length=16, default='')
    
    def __unicode__(self):
        return self.nama
        
    class Meta:
        verbose_name_plural = 'Daftar Pelanggan'

class Penjualan(models.Model):
    item = models.ForeignKey(Items, null=True)
    waktu_beli = models.DateTimeField('purchase date')
    harga = models.IntegerField()
    jumlah = models.IntegerField()
    user = models.ForeignKey(User)
    harga_total = models.IntegerField()
    pelanggan = models.ForeignKey(Pelanggan)
    kode = models.CharField(max_length=32)
    dll = models.CharField(max_length=32, default='')
    
    def __unicode__(self):
        return 'Penjualan %s (%d) %s' % (self.item.nama, self.jumlah, self.waktu_beli)
        
    class Meta:
        verbose_name_plural = 'Daftar Penjualan'
    
class Log(models.Model):
    nama = models.CharField(max_length=64)
    waktu_input = models.DateTimeField('add date')
    user = models.ForeignKey(User)
    data = models.TextField()
    
class Menu(models.Model):
    nama = models.CharField(max_length=32)
    group = models.IntegerField()
    link = models.CharField(max_length=32)
    status = models.IntegerField(default=1)
    
    class Meta:
        verbose_name_plural = 'Daftar Menu'
        
    def __unicode__(self):
        return self.nama
    
    def delete(self, *args, **kwargs):
        self.status = 0
        super(Menu, self).save(*args, **kwargs)
