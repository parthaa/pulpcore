# Generated by Django 2.2.11 on 2020-05-05 13:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0030_taskgroup_all_tasks_dispatched'),
    ]

    operations = [
        migrations.AlterField(
            model_name='export',
            name='task',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.Task'),
        ),
    ]