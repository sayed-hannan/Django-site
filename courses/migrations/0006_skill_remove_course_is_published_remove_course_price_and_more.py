# Generated by Django 4.2.4 on 2023-09-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_remove_course_modules'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='is_published',
        ),
        migrations.RemoveField(
            model_name='course',
            name='price',
        ),
        migrations.AddField(
            model_name='course',
            name='about',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='skills',
            field=models.ManyToManyField(blank=True, to='courses.skill'),
        ),
    ]