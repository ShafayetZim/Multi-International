# Generated by Django 4.0 on 2021-12-20 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_feature_alter_base_header_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feature',
            old_name='left_title',
            new_name='right_title',
        ),
    ]
