from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^login/$', views.login, name='login'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^movies/$', views.movies, name='movies'),
	url(r'^movie/(?P<movie_id>[0-9]+)/$', views.movie, name='movie'),
	url(r'^movie/(?P<movie_id>[0-9]+)/addfavorite/$', views.addfavorite, name='addfavorite'),
	url(r'^movie/(?P<movie_id>[0-9]+)/addwatched/$', views.addwatched, name='addwatched'),
	url(r'^movie/(?P<movie_id>[0-9]+)/addwished/$', views.addwished, name='addwished'),
	url(r'^favorite-movies/$', views.favorites, name='favorites'),
	url(r'^watched-movies/$', views.watched, name='watched'),
	url(r'^wished-movies/$', views.wished, name='wished'),
]
