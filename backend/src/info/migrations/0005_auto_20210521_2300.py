# Generated by Django 3.0.14 on 2021-05-21 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_auto_20210521_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourceimage',
            name='image',
            field=models.ImageField(upload_to='resources/images/95472960/'),
        ),
    ]
