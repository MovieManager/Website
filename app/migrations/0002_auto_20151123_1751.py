# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoritemovie',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='favoritemovie',
            name='user',
        ),
        migrations.RemoveField(
            model_name='watchedmovie',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='watchedmovie',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wishedmovie',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='wishedmovie',
            name='user',
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_movies',
            field=models.ManyToManyField(to='app.Movie'),
        ),
        migrations.DeleteModel(
            name='FavoriteMovie',
        ),
        migrations.DeleteModel(
            name='WatchedMovie',
        ),
        migrations.DeleteModel(
            name='WishedMovie',
        ),
    ]
