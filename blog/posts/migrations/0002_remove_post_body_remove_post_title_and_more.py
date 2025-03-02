# Generated by Django 5.1 on 2024-09-03 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='body',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='project_description',
            field=models.CharField(max_length=100000000, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='project_link',
            field=models.CharField(max_length=1000000, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='project_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
