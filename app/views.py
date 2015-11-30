from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import *
from django.utils import timezone

def index(request):
	return render(request, 'app/index.html', {})

def login(request):
	return render(request, 'app/login.html', {})

def signup(request):
	return render(request, 'app/signup.html', {})

def movies(request):
	movie_list = Movie.objects.order_by('-release_date')#[:5]
	return render(request, 'app/movies.html', {
		'movie_list': movie_list,
	})

def movie(request, movie_id):
	try:
		movie = Movie.objects.get(id = movie_id)
	except Movie.DoesNotExist:
		raise Http404('Movie does not exist')
	return render(request, 'app/movie.html', {
		'movie': movie,
	})
