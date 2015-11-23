from django.db import models

class Gender(models.Model):
	gender_name = models.CharField(max_length=200)
	def __str__(self):
		return self.gender_name

class Movie(models.Model):
	title = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	image_url = models.CharField(max_length=200)
	gender = models.ForeignKey(Gender)
	release_date = models.DateTimeField('date released')
	def __str__(self):
		return self.title

class User(models.Model):
	login = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	favorite_movies = models.ManyToManyField(Movie)
#	watched_movies = models.ManyToManyField(Movie)
#	wished_movies = models.ManyToManyField(Movie)
	def __str__(self):
		return self.login
