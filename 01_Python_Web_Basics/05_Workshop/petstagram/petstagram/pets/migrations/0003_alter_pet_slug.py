# Generated by Django 5.0 on 2023-12-16 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0002_pet_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
