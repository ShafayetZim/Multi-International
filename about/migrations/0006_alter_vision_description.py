# Generated by Django 3.2.9 on 2022-01-11 09:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_alter_about_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vision',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
