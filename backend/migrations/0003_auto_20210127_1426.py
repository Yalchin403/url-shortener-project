# Generated by Django 3.1.5 on 2021-01-27 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20210127_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='createdTime',
            field=models.DateTimeField(),
        ),
    ]
