# Generated by Django 4.0 on 2021-12-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('left_title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('icon', models.ImageField(upload_to='pics')),
            ],
        ),
        migrations.AlterField(
            model_name='base',
            name='header_phone',
            field=models.CharField(max_length=20),
        ),
    ]
