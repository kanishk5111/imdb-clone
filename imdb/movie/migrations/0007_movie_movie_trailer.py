# Generated by Django 3.1 on 2020-08-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
