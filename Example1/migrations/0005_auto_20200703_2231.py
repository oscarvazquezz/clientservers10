# Generated by Django 2.2.1 on 2020-07-04 03:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Example1', '0004_auto_20200703_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='example1',
            name='edad',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99), django.core.validators.MinLengthValidator(2)]),
        ),
    ]
