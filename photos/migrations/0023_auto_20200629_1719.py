# Generated by Django 3.0.6 on 2020-06-29 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0022_auto_20200629_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]
