# Generated by Django 2.0.7 on 2018-07-18 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='last_created',
            new_name='last_updated',
        ),
    ]
