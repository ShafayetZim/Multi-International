# Generated by Django 4.0 on 2021-12-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
                ('mail1', models.EmailField(max_length=254)),
                ('mail2', models.EmailField(max_length=254)),
                ('phone1', models.CharField(max_length=20)),
                ('phone2', models.CharField(max_length=20)),
            ],
        ),
    ]
