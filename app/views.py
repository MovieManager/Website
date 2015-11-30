from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import *
from django.utils import timezone

import sha
import urllib2, json

def dataFromUrl(url):
	response = urllib2.urlopen(url)
	return json.load(response)

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
	try:
		movie_list = []
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
