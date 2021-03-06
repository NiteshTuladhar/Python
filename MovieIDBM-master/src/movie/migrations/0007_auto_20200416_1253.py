# Generated by Django 3.0.3 on 2020-04-16 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20200414_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='category',
            field=models.CharField(choices=[('Action', 'ACTION'), ('Drama', 'DRAMA'), ('Comedy', 'COMEDY'), ('Romance', 'ROMANCE'), ('Horror', 'HORROR')], max_length=15),
        ),
        migrations.AlterField(
            model_name='movielinks',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='watch_movie_link', to='movie.Movie'),
        ),
    ]
