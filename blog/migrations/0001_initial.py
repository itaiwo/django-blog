# Generated by Django 4.2.7 on 2023-11-22 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('slug', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('author_img', models.CharField(max_length=50)),
                ('views', models.IntegerField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]
