from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
	url(r'^$', views.search, name='index'),
	url(r'^organisations/', views.search, name='search'),
	url(r'^results/', views.results, name='results'),
]

urlpatterns += staticfiles_urlpatterns()