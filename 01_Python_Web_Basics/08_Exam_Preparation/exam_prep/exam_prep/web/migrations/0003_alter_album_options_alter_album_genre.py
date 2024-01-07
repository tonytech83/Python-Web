# Generated by Django 5.0.1 on 2024-01-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_album_genre'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('pk',)},
        ),
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('POP', 'Pop Music'), ('JAZZ', 'Jazz Music'), ('RNB', 'R&B Music'), ('ROCK', 'Rock Music'), ('COUNTRY', 'Country Music'), ('DANCE', 'Dance Music'), ('HIP_HOP', 'Hip Hop Music'), ('OTHER', 'Other')], max_length=30),
        ),
    ]
