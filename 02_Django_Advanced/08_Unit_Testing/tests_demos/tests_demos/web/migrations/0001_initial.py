# Generated by Django 5.0.3 on 2024-03-30 07:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(choices=[('Fantasy', 'Fantasy'), ('Horror', 'Horror'), ('Action', 'Action'), ('Comedy', 'Comedy'), ('Romance', 'Romance'), ('Adventure', 'Adventure'), ('Thriller', 'Thriller')], default='Fantasy', max_length=9)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.author')),
            ],
        ),
    ]