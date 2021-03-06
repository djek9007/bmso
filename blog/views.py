from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View

from blog.models import Post, Category



class HomeView(View):
    def get(self, request):
        return render(request, 'blog/home.html',)

class PostListView(View):
    """Вывод категории и вывод стати"""

    # запрос к базе по полю публикации на true и по дате на сегодня которые должны выводится
    def get_queryset(self):
        return Post.objects.filter(published=True)

    def get(self, request, category_slug=None):
        # form = ContactForm()
        category = Category.objects.get(slug=self.kwargs['category_slug'])
        if category_slug is not None:
            posts = self.get_queryset().filter(category__slug=category_slug, category__published=True)
        else:
            posts = self.get_queryset()
        paginator = Paginator(posts, 12)
        page = self.request.GET.get('page')
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            posts = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            posts = paginator.page(paginator.num_pages)

        context = {
            'post_list': posts,
             'category': category,
            # 'form':form,
        }

        return render(request, 'blog/list.html', context)



class PostDetailView(View):
    """Полная статья одного статьи"""
    def get(self, request, **kwargs):
        post = get_object_or_404(Post, slug=kwargs.get("slug"))
        fileitems = post.fileitems.all()
        photoitems = post.photoitems.all()
        context = {
            'post': post,
            'fileitems':fileitems,
            'photoitems':photoitems,

        }
        return render(request, 'blog/detail.html', context)

    # def post(self, request, **kwargs):
    #
    #     post = get_object_or_404(Post, slug=kwargs.get("slug"))
    #     contact = Pages.objects.get(id=1)
    #     sent = False
    #     if request.method == 'POST':
    #         form = ContactForm(request.POST)
    #     # Если форма заполнена корректно, сохраняем все введённые пользователем значения
    #     if form.is_valid():
    #         cd = form.cleaned_data
    #         subject = 'Новый запрос от {} по почте {}'.format(cd['name'], cd['email'])
    #         sender = cd['email']
    #         phone = cd['phone']
    #         message = 'Имя клиента: {} \nТелефон клиента: {} \nПочта клиента: {}\nТекст запроса: {}\n{} Со страницы'.format(
    #             cd['name'], cd['phone'], cd['email'], cd['message'], post)
    #
    #         recipients = ['zakaz@mnka.kz']
    #         # Если пользователь захотел получить копию себе, добавляем его в список получателей
    #         # if copy:
    #         #     recipients.append(sender)
    #         try:
    #             send_mail(subject, message, 'zakaz@mnka.kz', recipients)
    #             sent = True
    #         except BadHeaderError:  # Защита от уязвимости
    #             return HttpResponse('Invalid header found')
    #         # Переходим на другую страницу, если сообщение отправлено
    #         context = {
    #             'contact': contact,
    #             'form': form,
    #             'sent': sent, }
    #         return render(request, 'blog/detail.html', context)
    #     else:
    #         # Заполняем форму
    #         form = ContactForm()
    #     return render(request, 'blog/detail.html', context)

