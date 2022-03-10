from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic.base import View

from gallery.models import Year, Albom

class GalleryView(View):

    def get_queryset(self):
        return Year.objects.filter(published=True)

    def get(self, request, ):
        year = self.get_queryset()
        paginator = Paginator(year, 12)
        page = self.request.GET.get('page')
        try:
            year = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            year = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            year = paginator.page(paginator.num_pages)

        context = {
            'year_list': year,
        }

        return render(request, 'gallery/list_gallery.html', context)

class GalleryListView(View):
    """Вывод категории и вывод стати"""

    # запрос к базе по полю публикации на true и по дате на сегодня которые должны выводится
    def get_queryset(self):
        return Albom.objects.filter(published=True)

    def get(self, request, year_slug=None):
        # form = ContactForm()
        year = Year.objects.get(slug=self.kwargs['year_slug'])
        if year_slug is not None:
            posts = self.get_queryset().filter(year__slug=year_slug, )
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
            'year': year,
            # 'form':form,
        }

        return render(request, 'gallery/list_gallery.html', context)

class GalleryDetailView(View):
    """Полная статья одного статьи"""
    def get(self, request, **kwargs):
        post = get_object_or_404(Albom, slug=kwargs.get("albom_slug"))
        photoitems = post.photoitems.all()
        context = {
                'post': post,
                'photoitems':photoitems,

        }
        return render(request, 'gallery/detail_gallery.html', context)

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

