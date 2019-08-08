# Generated by Django 2.2.4 on 2019-08-07 10:38

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='country_ethnicity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country_ethnicity', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='drug',
            fields=[
                ('drug_id', models.AutoField(primary_key=True, serialize=False)),
                ('drug_name', models.CharField(max_length=250)),
                ('posology', models.CharField(default='NA', max_length=250)),
                ('chemical_structure', models.TextField(default='NA')),
                ('drug_bank_id', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='drug_state',
            fields=[
                ('state_id', models.AutoField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='externalid_type',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='pharmacogenes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('gene_name', models.CharField(max_length=50)),
                ('protein', models.CharField(default='NA', max_length=50)),
                ('function', models.TextField(default='NA')),
            ],
        ),
        migrations.CreateModel(
            name='snp',
            fields=[
                ('snp_id', models.AutoField(primary_key=True, serialize=False)),
                ('rs_id', models.CharField(max_length=50)),
                ('allele', models.CharField(max_length=50)),
                ('disease_phenotype', models.TextField()),
                ('chromosome', models.CharField(max_length=50)),
                ('p_value', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=10)),
                ('drug', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agmp_app.drug')),
                ('gene', models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='agmp_app.pharmacogenes')),
            ],
        ),
        migrations.CreateModel(
            name='star_allele',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('star_annotation', models.CharField(max_length=50)),
                ('disease_phenotype', models.CharField(max_length=50)),
                ('chromosome', models.CharField(max_length=50)),
                ('p_value', models.DecimalField(decimal_places=4, default=Decimal('0.0000'), max_digits=10)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agmp_app.drug')),
                ('gene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agmp_app.pharmacogenes')),
            ],
        ),
        migrations.CreateModel(
            name='study',
            fields=[
                ('study_id', models.AutoField(primary_key=True, serialize=False)),
                ('study_title', models.CharField(max_length=250)),
                ('external_id', models.CharField(max_length=50)),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='star_allele_ethnicity_country',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country_ethnicity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agmp_app.country_ethnicity')),
                ('star_allele_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agmp_app.star_allele')),
            ],
        ),
        migrations.AddField(
            model_name='star_allele',
            name='reference',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agmp_app.study'),
        ),
        migrations.CreateModel(
            name='snp_country_ethnicity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country_ethnicity_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agmp_app.country_ethnicity')),
                ('snp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agmp_app.snp')),
            ],
        ),
        migrations.AddField(
            model_name='snp',
            name='reference',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='agmp_app.study'),
        ),
        migrations.AddField(
            model_name='drug',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agmp_app.drug_state'),
        ),
    ]
