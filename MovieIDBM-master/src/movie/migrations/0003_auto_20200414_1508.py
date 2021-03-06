# Generated by Django 3.0.3 on 2020-04-14 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_auto_20200414_1459'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MovieLinka',
            new_name='MovieLinks',
        ),
        migrations.AlterField(
            model_name='movielinks',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_movie_link', to='movie.Movie'),
        ),
    ]
