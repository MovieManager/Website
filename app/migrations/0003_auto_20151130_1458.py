# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20151123_1751'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteMovie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ext_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WatchedMovie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ext_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='WishedMovie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ext_id', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='gender',
        ),
        migrations.AlterField(
            model_name='user',
            name='favorite_movies',
            field=models.ManyToManyField(to='app.FavoriteMovie'),
        ),
        migrations.DeleteModel(
            name='Gender',
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.AddField(
            model_name='user',
            name='watched_movies',
            field=models.ManyToManyField(to='app.WatchedMovie'),
        ),
        migrations.AddField(
            model_name='user',
            name='wished_movies',
            field=models.ManyToManyField(to='app.WishedMovie'),
        ),
    ]
