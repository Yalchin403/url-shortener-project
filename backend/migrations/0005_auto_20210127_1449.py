# Generated by Django 3.1.5 on 2021-01-27 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20210127_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shortenedurl',
            name='shortnedUrl',
        ),
        migrations.AddField(
            model_name='shortenedurl',
            name='shortenedUrl',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]
