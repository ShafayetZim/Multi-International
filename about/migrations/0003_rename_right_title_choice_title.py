# Generated by Django 4.0 on 2021-12-21 07:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_about_shape'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='right_title',
            new_name='title',
        ),
    ]