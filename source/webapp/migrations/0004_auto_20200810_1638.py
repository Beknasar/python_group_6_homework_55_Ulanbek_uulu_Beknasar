# Generated by Django 2.2 on 2020-08-10 16:38

from django.db import migrations

def transfer_types(apps, schema_editor):
    Task = apps.get_model('webapp.Tasks')
    for task in Task.objects.all():
        task.types.add(task.type_old)

class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_tasks_types'),
    ]

    operations = [
        migrations.RunPython(transfer_types, migrations.RunPython.noop)
    ]
