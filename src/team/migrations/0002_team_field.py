# Generated by Django 3.0.4 on 2020-06-09 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='field',
            field=models.CharField(default='asd', max_length=10),
        ),
    ]
