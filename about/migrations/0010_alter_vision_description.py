# Generated by Django 3.2.9 on 2022-01-11 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_alter_vision_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vision',
            name='description',
            field=models.TextField(),
        ),
    ]
