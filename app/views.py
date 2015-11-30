from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import *
from django.utils import timezone

def index(request):
	template = loader.get_template('app/index.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def login(request):
	template = loader.get_template('app/login.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def signup(request):
	template = loader.get_template('app/signup.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def movies(request):
	movie_list = Movie.objects.order_by('-release_date')#[:5]
	template = loader.get_template('app/movies.html')
	context = RequestContext(request, {
		'movie_list': movie_list,
	})
	return HttpResponse(template.render(context))

def movie(request, movie_id):
	movie = Movie.objects.get(id = movie_id)
	template = loader.get_template('app/movie.html')
	context = RequestContext(request, {
		'movie': movie,
	})
	return HttpResponse(template.render(context))
