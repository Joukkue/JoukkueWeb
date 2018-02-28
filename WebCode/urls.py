from django.conf.urls import url
from WebCode.myviews   import front

urlpatterns = [
    url(r'^$', front.frontpage, name = 'home'),
    url(r'^home/$', front.frontpage, name = 'home'),
    url(r'^quotes/$', front.show, name = 'quotes'),
]