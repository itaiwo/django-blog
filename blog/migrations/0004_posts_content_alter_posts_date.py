# Generated by Django 4.2.7 on 2023-11-22 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_author_post_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='content',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='posts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 22, 10, 44, 5, 819502)),
        ),
    ]
