from . import views
from django.urls import path
app_name = 'gallery'
urlpatterns = [
    path('', views.GalleryView.as_view(), name='show'),
    path('<slug:year_slug>/', views.GalleryListView.as_view(), name='gallery_list'),
    path('<slug:year_slug>/<slug:albom_slug>/', views.GalleryDetailView.as_view(), name='gallery_detail'),

]