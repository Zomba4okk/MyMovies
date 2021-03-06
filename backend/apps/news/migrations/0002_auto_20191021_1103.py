# Generated by Django 2.2.4 on 2019-10-21 11:03

import apps.utils
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsimage',
            name='image_file',
            field=models.ImageField(null=True, upload_to=apps.utils.SetAddressFunctionsClass.set_address_for_file_field),
        ),
        migrations.AlterField(
            model_name='newsmainimage',
            name='image_file',
            field=models.ImageField(null=True, upload_to=apps.utils.SetAddressFunctionsClass.set_address_for_file_field),
        ),
    ]
