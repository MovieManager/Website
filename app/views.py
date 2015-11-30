from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import *
from django.utils import timezone
from django.template.defaulttags import register

import sha
import urllib2, json

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
		parameter_values.append(key + '=' + parameters[key])
	parameters_string = '&'.join(parameter_values)
	url = '%s%s?%s' % (API_URL, url, parameters_string)
	return dataFromUrl(url)

def getMovie(movieId):
	return getAPIData('/movie/' + movieId, {})

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
			return HttpResponseRedirect('/app/login/')
	return render(request, 'app/signup.html', {})

def movies(request):
	results = getAPIData('/discover/movie', {
		'sort_by': 'popularity.desc'
	})['results']
	return render(request, 'app/movies.html', {
		'movie_list': results,
	})

def movie(request, movie_id):
	movie = getMovie(movie_id)
	return render(request, 'app/movie.html', {
		'movie': movie,
	})

def favorites(request):
	try:
		movie_list = []
	except Movie.DoesNotExist:
		raise Http404('Movie does not exist')
	return render(request, 'app/movies.html', {
		'movie_list': movie_list,
	})

def watched(request):
	try:
		movie_list = []
	except Movie.DoesNotExist:
		raise Http404('Movie does not exist')
	return render(request, 'app/movies.html', {
		'movie_list': movie_list,
	})

def wished(request):
	try:
		movie_list = []
	except Movie.DoesNotExist:
		raise Http404('Movie does not exist')
	return render(request, 'app/movies.html', {
		'movie_list': movie_list,
	})
