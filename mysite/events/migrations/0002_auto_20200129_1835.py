# Generated by Django 3.0.2 on 2020-01-29 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='Category',
            new_name='category',
        ),
    ]