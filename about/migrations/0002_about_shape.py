# Generated by Django 4.0 on 2021-12-21 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='shape',
            field=models.ImageField(default=0, upload_to='about'),
            preserve_default=False,
        ),
    ]
