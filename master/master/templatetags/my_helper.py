from django import template
from products.models import Items

register = template.Library()

@register.filter(name='create_range')
def create_range(val):
    '''
        create range'''
        
    return range(val)


@register.filter(name='get_item_by_type')
def get_item_by_type(tipe, skip=4):
    
    try:
        items = Items.objects.filter(tipe_item__nama=tipe).order_by('-waktu_modif')[:skip]
    except:
        items = {}
        
    return items
    
@register.filter(name='get_total_item')
def get_total_item(tipe=''):
    if not tipe:
        length = len(Items.objects.all())
    else:
        try:
            length  = len(Items.objects.filter(tipe_item__nama=tipe))
        except:
            length = 0
            
    return length

@register.filter(name="with_brace")
def with_brace(char):
    return "{{" + str(char) + "}}"
