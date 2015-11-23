# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteMovie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gender_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('image_url', models.CharField(max_length=200)),
                ('release_date', models.DateTimeField(verbose_name=b'date released')),
                ('gender', models.ForeignKey(to='app.Gender')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('login', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WatchedMovie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie', models.ForeignKey(to='app.Movie')),
                ('user', models.ForeignKey(to='app.User')),
            ],
        ),
        migrations.CreateModel(
            name='WishedMovie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('movie', models.ForeignKey(to='app.Movie')),
                ('user', models.ForeignKey(to='app.User')),
            ],
        ),
        migrations.AddField(
            model_name='favoritemovie',
            name='movie',
            field=models.ForeignKey(to='app.Movie'),
        ),
        migrations.AddField(
            model_name='favoritemovie',
            name='user',
            field=models.ForeignKey(to='app.User'),
        ),
    ]
