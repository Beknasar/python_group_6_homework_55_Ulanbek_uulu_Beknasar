# Generated by Django 2.2 on 2020-08-10 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='type',
            new_name='type_old',
        ),
    ]
