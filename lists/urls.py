from django.conf.urls import url
from lists import views

urlpatterns = [
    url(r'^new$', views.new_lists, name='new_list'),
    url(r'^(\d+)/$', views.view_list, name='view_list'),
    url(r'^(\d+)/add_item$', views.add_item, name='add_item'),
]
