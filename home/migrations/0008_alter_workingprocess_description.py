# Generated by Django 3.2.9 on 2022-01-12 05:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_slider_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workingprocess',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
