# Generated by Django 2.2.3 on 2019-08-01 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='subscribe_end',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='subscribe_start',
            field=models.DateField(null=True),
        ),
    ]