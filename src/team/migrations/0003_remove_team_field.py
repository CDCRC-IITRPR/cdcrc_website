# Generated by Django 3.0.4 on 2020-06-09 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_team_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='field',
        ),
    ]