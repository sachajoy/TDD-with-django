from django.conf.urls import url, include
from lists import views
from lists import urls

urlpatterns = [
    url(r'^$', views.home_page, name='home'),
    url(r'^lists/', include(urls)),
]
