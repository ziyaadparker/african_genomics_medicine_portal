# Generated by Django 2.2.2 on 2019-08-05 20:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agmp_app', '0002_auto_20190805_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='study',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
