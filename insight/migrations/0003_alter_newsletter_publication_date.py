# Generated by Django 4.2.4 on 2023-09-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insight', '0002_newsletter_image_alter_newsletter_publication_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='publication_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]