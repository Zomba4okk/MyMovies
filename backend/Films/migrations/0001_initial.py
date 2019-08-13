# Generated by Django 2.2.3 on 2019-07-23 07:26

import Films.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('poster', models.ImageField(upload_to=Films.models.get_film_poster_address)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('average_rate', models.IntegerField(default=0)),
                ('age_rate', models.IntegerField()),
                ('film_file', models.FileField(upload_to=Films.models.get_film_address)),
                ('film_company', models.CharField(max_length=50)),
                ('producing_country', models.CharField(max_length=50)),
                ('producer', models.CharField(max_length=50)),
                ('duration', models.DurationField()),
                ('premiere', models.DateField()),
                ('views_count', models.IntegerField(default=0)),
                ('visits_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Trailer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('trailer', models.FileField(null=True, upload_to=Films.models.get_film_trailer_address)),
                ('short_description', models.TextField(blank=True, max_length=200)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trailers', to='Films.Film')),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField()),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Films.Film')),
                ('user', models.ManyToManyField(related_name='marks', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('film', models.ManyToManyField(related_name='languages', to='Films.Film')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('film', models.ManyToManyField(related_name='genres', to='Films.Film')),
            ],
        ),
        migrations.CreateModel(
            name='FilmImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=Films.models.get_film_image_address)),
                ('short_description', models.TextField(blank=True, max_length=200)),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='Films.Film')),
            ],
        ),
    ]