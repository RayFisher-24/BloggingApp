# Generated by Django 3.0.6 on 2020-06-24 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20200624_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='wedding',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='pics')),
                ('cw', models.CharField(default='None', max_length=20)),
            ],
        ),
    ]
