# Generated by Django 4.2.4 on 2023-09-07 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0005_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='image',
        ),
    ]
