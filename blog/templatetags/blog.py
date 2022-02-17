from django import template

from blog.models import Post
from menu.models import Menu
from slide.models import Slide

register = template.Library()



def get_news_in_main():
    """QuerySet menu item"""
    return Post.objects.filter(
            published=True,
            category=6,
        )



@register.simple_tag(takes_context=True)
def show_news(context, ):
    """Вывод меню без шаблона"""
    return get_news_in_main()

@register.simple_tag(takes_context=True)
def show_slider(context, ):
    """Вывод меню без шаблона"""
    return Slide.objects.filter(
        published=True
    )
