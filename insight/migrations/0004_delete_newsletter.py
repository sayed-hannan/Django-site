# Generated by Django 4.2.4 on 2023-09-07 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0003_alter_newsletter_publication_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Newsletter',
        ),
    ]
