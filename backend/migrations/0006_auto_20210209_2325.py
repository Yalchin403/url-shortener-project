# Generated by Django 3.1.5 on 2021-02-09 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20210127_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenedurl',
            name='createdTime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]