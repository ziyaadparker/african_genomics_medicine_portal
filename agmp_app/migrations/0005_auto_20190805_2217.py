# Generated by Django 2.2.2 on 2019-08-05 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agmp_app', '0004_remove_study_externalid_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snp',
            name='drug_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agmp_app.drug'),
        ),
        migrations.AlterField(
            model_name='snp',
            name='gene_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agmp_app.pharmacogenes'),
        ),
        migrations.AlterField(
            model_name='snp',
            name='reference_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='agmp_app.study'),
        ),
    ]
