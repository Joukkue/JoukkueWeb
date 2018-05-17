from django.conf.urls import url, re_path
from WebCode.myviews   import front
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^$', front.frontpage, name = 'home'),
    url(r'^home/$', front.frontpage, name = 'home'),
    url(r'^login/$', front.login_user,  name = 'login'),
    url(r'^logout/$', front.logout_user,  name = 'logout'),
    url(r'^quotes/$', front.show, name = 'quotes'),
    url(r'^loginpage/$', front.login_page,  name = 'loginpage'),
    url(r'^signup/$', front.signup, name = 'signup'),
    url(r'^levels/$', front.get_levels, name = 'levels'),
    re_path('react', TemplateView.as_view(template_name='index.html')),

]