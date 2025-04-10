# Generated by Django 4.2.20 on 2025-04-09 03:51

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Miles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('begin', models.DecimalField(decimal_places=1, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('end', models.DecimalField(decimal_places=1, max_digits=10, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('total', models.DecimalField(decimal_places=1, editable=False, max_digits=10, null=True)),
                ('invoice', models.CharField(blank=True, max_length=255, null=True)),
                ('tax', models.CharField(default='Yes', max_length=10, null=True)),
                ('job', models.CharField(blank=True, max_length=255, null=True)),
                ('vehicle', models.CharField(default='Lead Foot', max_length=255, null=True)),
                ('mileage_type', models.CharField(choices=[('Taxable', 'Taxable'), ('Reimbursed', 'Reimbursed')], default='Taxable', max_length=20)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.client')),
            ],
            options={
                'verbose_name_plural': 'Miles',
                'ordering': ['-date'],
            },
        ),
    ]
