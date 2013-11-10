from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ItemType(models.Model):
    name = models.CharField(max_length=32)
    real_name = models.CharField(max_length=32)
    add_date = models.DateTimeField('date adding', default=timezone.now)
    
    def __unicode__(self):
        return self.real_name.capitalize()
    
    class Meta:
        verbose_name_plural = 'Jenis item'
    

class Items(models.Model):
    name = models.CharField(max_length=64)
    add_date = models.DateTimeField('date adding')
    mod_date = models.DateTimeField('date modified')
    item_type = models.ForeignKey(ItemType)
    user = models.ForeignKey(User)
    sell_price = models.IntegerField()
    purchase_price = models.IntegerField()
    stock = models.IntegerField(default=0)
    
    def __unicode__(self):
        return '(%s) - %s' % (self.item_type.real_name, self.name)
        
    class Meta:
        verbose_name_plural = 'Daftar Item'
