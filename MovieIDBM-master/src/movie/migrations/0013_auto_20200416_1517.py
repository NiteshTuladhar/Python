# Generated by Django 3.0.3 on 2020-04-16 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0012_auto_20200416_1505'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movieslug',
            name='id',
        ),
        migrations.AddField(
            model_name='movieslug',
            name='movie_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='movie.Movie'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movielinks',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_watch_link', to='movie.Movie'),
        ),
        migrations.AlterField(
            model_name='movieslug',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='movie_slug', to='movie.Movie'),
        ),
    ]