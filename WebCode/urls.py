from django.conf.urls import url
from WebCode.myviews   import front
from WebCode.suprise.views import view1, clue, view2, clue2

urlpatterns = [
    url(r'^$', front.frontpage, name = 'home'),
    url(r'^home/$', front.frontpage, name = 'home'),
    url(r'^login/$', front.login_user,  name = 'login'),
    url(r'^logout/$', front.logout_user,  name = 'logout'),
    url(r'^quotes/$', front.show, name = 'quotes'),
    url(r'^loginpage/$', front.login_page,  name = 'loginpage'),
    url(r'^signup/$', front.signup, name = 'signup'),
    url(r'^levels/$', front.get_levels, name = 'levels'),
    url(r'^jennanlahja/$', view1, name='lahja1'),
    url(r'^valtterinpaketti/$', view2, name='lahja2'),
    url(r'^credentials/$', clue),
    url(r'^details/$', clue2),
]