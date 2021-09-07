from django.conf.urls import url
from .views import *
app_name = 'post'
urlpatterns = [

    url(r'^index/$', post_index, name='index'), #sol da adres sağda da adreste çalışacak view(görüntünün) ismi
    url(r'^create/$', post_create, name='create'),
    url(r'^hakkimda/$', post_hakkimda, name='hakkimda'),
    url(r'^iletisim/$', post_iletisim, name='iletisim'),
    url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/update/$', post_update, name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', post_delete, name='delete'),

]