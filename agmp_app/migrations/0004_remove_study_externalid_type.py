# Generated by Django 2.2.2 on 2019-08-05 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agmp_app', '0003_auto_20190805_2035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='study',
            name='externalid_type',
        ),
    ]
