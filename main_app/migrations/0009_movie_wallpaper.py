# Generated by Django 3.2.1 on 2022-08-14 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_alter_movie_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='wallpaper',
            field=models.ImageField(default='wall.jpg', upload_to='images/movie_walls/'),
        ),
    ]