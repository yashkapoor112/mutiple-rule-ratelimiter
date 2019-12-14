from django.conf.urls import url

from kills import views

urlpatterns = [

    url(r'^add/dragon/$', views.register_dragon, name='register_dragon'),
    url(r'^add/rule/$', views.add_rule, name='add_rule'),
    url(r'^delete/rule/$', views.delete_rule, name='delete_rule'),
    url(r'^kill/animal/$', views.kill_animal, name='kill_animal'),
]