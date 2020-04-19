# Generated by Django 3.0.3 on 2020-04-16 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0016_auto_20200416_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='banner',
            field=models.ImageField(default='', upload_to='movies_banner'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movielinks',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_watch_link', to='movie.Movie'),
        ),
    ]
