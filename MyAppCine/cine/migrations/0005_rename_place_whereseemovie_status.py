# Generated by Django 4.1.5 on 2023-01-29 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0004_alter_film_director_director_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='whereseemovie',
            old_name='place',
            new_name='status',
        ),
    ]
