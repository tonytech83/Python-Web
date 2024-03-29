# Generated by Django 5.0.1 on 2024-02-06 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=35)),
                ('last_name', models.CharField(max_length=35)),
                ('role', models.IntegerField(choices=[(1, 'Software Engineer'), (2, 'Developer'), (3, 'QA Engineer')])),
            ],
        ),
    ]
