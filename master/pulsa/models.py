from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pulsa(models.Model):
    name = models.CharField(max_length=64)
    add_date = models.DateTimeField('date adding')
    mod_date = models.DateTimeField('date modified', auto_now=True)
    status = models.BooleanField()
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Daftar Pulsa'
