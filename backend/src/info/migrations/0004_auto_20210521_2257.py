# Generated by Django 3.0.14 on 2021-05-21 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_auto_20210521_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourceimage',
            name='image',
            field=models.ImageField(upload_to='resources/images/30927086/'),
        ),
    ]