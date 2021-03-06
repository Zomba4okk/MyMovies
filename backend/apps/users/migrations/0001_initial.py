# Generated by Django 2.2.4 on 2019-10-21 09:26

import apps.users.validators
import apps.utils
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(default='user', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, error_messages={'unique': 'This username is already taken.'}, max_length=50, unique=True, validators=[apps.users.validators.UsernameValidator()])),
                ('avatar', models.ImageField(upload_to=apps.utils.SetAddressFunctionsClass.set_address_for_file_field)),
                ('email', models.EmailField(db_index=True, error_messages={'unique': 'This email address is already used.'}, max_length=254, unique=True)),
                ('full_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('birthday', models.DateField(validators=[apps.users.validators.validate_birthday])),
                ('country', models.CharField(max_length=50)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_subscribed', models.BooleanField(default=False)),
                ('subscribe_start', models.DateField(null=True)),
                ('subscribe_end', models.DateField(null=True)),
                ('reviews_number', models.IntegerField(default=0)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_permission', to='users.UserPermission')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
