from django import template

from blog.models import Post


register = template.Library()



def get_news_in_main():
    """QuerySet menu item"""
    return Post.objects.filter(
            published=True,
            category=5,
        )[:5]



@register.simple_tag(takes_context=True)
def show_news(context, ):
    """Вывод меню без шаблона"""
    return get_news_in_main()


