from django import template

register = template.Library()

@register.filter(name='create_range')
def create_range(val):
    '''
        create range'''
        
    return range(val)
