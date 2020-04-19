# Generated by Django 3.0.3 on 2020-04-16 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20200416_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='movie_trailer',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movielinks',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_movie_link', to='movie.Movie'),
        ),
    ]
