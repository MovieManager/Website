from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import *
from django.utils import timezone

def index(request):
	return render(request, 'app/index.html', {})

def login(request):
	return render(request, 'app/login.html', {})

def signup(request):
	return render(request, 'app/signup.html', {})

def movies(request):
	try:
		movie_list = Movie.objects.order_by('-release_date')
	except Movie.DoesNotExist:
		raise Http404('Movie does not exist')
	return render(request, 'app/movies.html', {
		'movie_list': movie_list,
	})

def movie(request, movie_id):
	movie = get_object_or_404(Movie, id = movie_id)
	return render(request, 'app/movie.html', {
		'movie': movie,
	})
