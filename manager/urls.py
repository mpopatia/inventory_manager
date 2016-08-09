from django.conf.urls import url
from manager import views

urlpatterns = [url(r'^$', views.index, name='index'),
               url(r'^get_items', views.get_items, name='get_items'),]
