from django import template

from slide.models import Slide

register = template.Library()
def get_slider():
    """Получение слайдера"""
    return Slide.objects.all()

@register.simple_tag(takes_context=True)
def show_slider(context, ):
    """Вывод меню без шаблона"""
    return get_slider()