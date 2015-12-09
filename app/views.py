from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import *
from django.utils import timezone
from django.template.defaulttags import register

import sha
import urllib, urllib2, json

API_URL = 'http://api.themoviedb.org/3'
API_KEY = 'c98f210d025999131d6987d08f8eecd8'

@register.filter
def get_value(dictionary, key):
	return dictionary.get(key)

def dataFromUrl(url):
	response = urllib2.urlopen(url)
	return json.load(response)

def getAPIData(url = '/', parameters = {}):
	parameters['api_key'] = API_KEY
	parameter_values = []
	for key in parameters:
		parameter_values.append(key + '=' + urllib.quote(parameters[key]))
	parameters_string = '&'.join(parameter_values)
	url = '%s%s?%s' % (API_URL, url, parameters_string)
	return dataFromUrl(url)

def getMovie(movieId):
	return getAPIData('/movie/%d' % int(movieId), {})

def index(request):
	return render(request, 'app/index.html', {})

def login(request):
	if len(request.POST) > 0:
		login = request.POST['login']
		password = request.POST['password']
		password_hash = sha.new(password).hexdigest()
		users = User.objects.filter(login = login)
		user = None
		if len(users) > 0:
			user = users[0]
		error_message = None
		if login == '':
			error_message = 'Please specify a login'
		elif password == '':
			error_message = 'Please specify a password'
		elif user != None:
			if user.password != password_hash:
				error_message = 'Password is incorrect'
		else:
			error_message = 'User "%s" does not exist' % login
		if error_message != None:
			return render(request, 'app/login.html', {
				'error_message': error_message,
			})
		else:
			return HttpResponseRedirect('/app/')
	return render(request, 'app/login.html', {})

def signup(request):
	if len(request.POST) > 0:
		login = request.POST['login']
		password = request.POST['password']
		users = User.objects.filter(login = login)
		error_message = None
		if login == '':
			error_message = 'Please specify a login'
		elif password == '':
			error_message = 'Please specify a password'
		elif len(users) != 0:
			error_message = 'User "%s" already exists' % login
		if error_message:
			return render(request, 'app/signup.html', {
				'error_message': error_message,
			})
		else:
			password_hash = sha.new(password).hexdigest()
			User(login = login, password = password_hash).save()
			return HttpResponseRedirect('/app/')
	return render(request, 'app/signup.html', {})

def movies(request):
	results = []
	search_text = None
	search_date = None
	search_genre = None
	if len(request.POST) > 0:
		search_text = request.POST['search_text']
		search_date = request.POST['search_date']
		search_genre = request.POST['search_genre']
		if search_text == '':
			search_text = None
		if search_date == '':
			search_date = None
		if search_genre == '':
			search_genre = None
	if search_text != None:
		results = getAPIData('/search/movie', {
			'query': search_text
		})['results']
	else:
		params = {
			'sort_by': 'popularity.desc'
		}
		if search_date != None:
			params['release_date.gte'] = search_date + '-01-01'
			params['release_date.lte'] = search_date + '-12-31'
		results = getAPIData('/discover/movie', params)['results']
	years = range(1970,2016)
	return render(request, 'app/movies.html', {
		'movie_list': results,
		'year_list' : years,
		'search_bar': True,
		'search_text': search_text if search_text else ''
	})

def movie(request, movie_id):
	movie = getMovie(movie_id)
	return render(request, 'app/movie.html', {
		'movie': movie,
	})

def favorites(request):
	movies = []
	favoriteMovies = User.objects.get(id = 1).favorite_movies.all()
	for favoriteMovie in favoriteMovies:
		movies.append(getMovie(favoriteMovie.ext_id))
	return render(request, 'app/movies.html', {
		'movie_list': movies,
	})

def watched(request):
	movies = []
	watchedMovies = User.objects.get(id = 1).watched_movies.all()
	for watchedMovie in watchedMovies:
		movies.append(getMovie(watchedMovie.ext_id))
	return render(request, 'app/movies.html', {
		'movie_list': movies,
	})

def wished(request):
	movies = []
	wishedMovies = User.objects.get(id = 1).wished_movies.all()
	for wishedMovie in wishedMovies:
		movies.append(getMovie(wishedMovie.ext_id))
	return render(request, 'app/movies.html', {
		'movie_list': movies,
	})

def addfavorite(request, movie_id):
	favoriteMovies = FavoriteMovie.objects.filter(ext_id = movie_id)
	if len(favoriteMovies) == 0:
		FavoriteMovie(ext_id = movie_id).save()
	favoriteMovie = None
	favoriteMovies = FavoriteMovie.objects.filter(ext_id = movie_id)
	if len(favoriteMovies) > 0:
		favoriteMovie = favoriteMovies[0]
	User.objects.get(id = 1).favorite_movies.add(favoriteMovie)
	return HttpResponseRedirect('/app/')

def addwatched(request, movie_id):
	watchedMovies = WatchedMovie.objects.filter(ext_id = movie_id)
	if len(watchedMovies) == 0:
		WatchedMovie(ext_id = movie_id).save()
	watchedMovie = None
	watchedMovies = WatchedMovie.objects.filter(ext_id = movie_id)
	if len(watchedMovies) > 0:
		watchedMovie = watchedMovies[0]
	User.objects.get(id = 1).watched_movies.add(watchedMovie)
	return HttpResponseRedirect('/app/')

def addwished(request, movie_id):
	wishedMovies = WishedMovie.objects.filter(ext_id = movie_id)
	if len(wishedMovies) == 0:
		WishedMovie(ext_id = movie_id).save()
	wishedMovie = None
	wishedMovies = WishedMovie.objects.filter(ext_id = movie_id)
	if len(wishedMovies) > 0:
		wishedMovie = wishedMovies[0]
	User.objects.get(id = 1).wished_movies.add(wishedMovie)
	return HttpResponseRedirect('/app/')
