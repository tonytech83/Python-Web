# Generated by Django 5.0.2 on 2024-02-13 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_todo_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='tenant',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
    ]
