from django import template

from menu.models import Menu

register = template.Library()



def get_menu_item():
    """QuerySet menu item"""
    return Menu.objects.filter(
            published=True
        )



@register.simple_tag(takes_context=True)
def show_menu(context, ):
    """Вывод меню без шаблона"""
    return get_menu_item()

