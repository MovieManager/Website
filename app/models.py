from django.db import models

class FavoriteMovie(models.Model):
	ext_id = models.IntegerField()
	def __str__(self):
		return 'Movie' + self.ext_id

class WatchedMovie(models.Model):
	ext_id = models.IntegerField()
	def __str__(self):
		return 'Movie' + self.ext_id

class WishedMovie(models.Model):
	ext_id = models.IntegerField()
	def __str__(self):
		return 'Movie' + self.ext_id

class User(models.Model):
	login = models.CharField(max_length=200)
	password = models.CharField(max_length=200)
	favorite_movies = models.ManyToManyField(FavoriteMovie)
	watched_movies = models.ManyToManyField(WatchedMovie)
	wished_movies = models.ManyToManyField(WishedMovie)
	def __str__(self):
		return self.login
