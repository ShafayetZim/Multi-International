# Generated by Django 3.2.9 on 2022-01-11 11:11

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0008_alter_vision_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vision',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
