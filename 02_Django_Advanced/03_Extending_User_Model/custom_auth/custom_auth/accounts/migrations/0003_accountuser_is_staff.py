# Generated by Django 5.0.3 on 2024-03-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_accountuser_managers_accountuser_date_joined_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
