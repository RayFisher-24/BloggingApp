# Generated by Django 3.0.6 on 2020-06-25 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0005_wedding'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='cf',
            new_name='alt',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='cp',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='cw',
        ),
    ]
