# Generated by Django 2.2.14 on 2020-07-22 19:50

from django.db import migrations, models
import pulpcore.app.models.content
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_unprotect_last_export'),
    ]

    operations = [
        migrations.CreateModel(
            name='PulpTemporaryFile',
            fields=[
                ('pulp_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('pulp_created', models.DateTimeField(auto_now_add=True)),
                ('pulp_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('file', models.FileField(max_length=255, upload_to=pulpcore.app.models.content.PulpTemporaryFile.storage_path)),
            ],
            options={
                'abstract': False,
            },
            bases=(pulpcore.app.models.content.HandleTempFilesMixin, models.Model),
        ),
    ]
