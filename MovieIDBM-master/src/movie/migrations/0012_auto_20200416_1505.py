# Generated by Django 3.0.3 on 2020-04-16 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0011_auto_20200416_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='slug',
        ),
        migrations.AlterField(
            model_name='movie',
            name='movie_trailer',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='movielinks',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_watch_link', to='movie.Movie'),
        ),
        migrations.CreateModel(
            name='MovieSlug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_slug', to='movie.Movie')),
            ],
        ),
    ]
