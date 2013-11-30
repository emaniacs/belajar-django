from django import template
from products.models import Menu

register = template.Library()

@register.filter(name="get_menu")
def get_menu(name):
    '''
    '''
        
    menus = Menu.objects.filter(status=1)
    for menu in menus:
        if menu.nama.lower() == name:
            menu.status = 'active'
        else:
            menu.status = ''
    return menus
