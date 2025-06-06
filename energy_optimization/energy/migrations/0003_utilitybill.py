# Generated by Django 5.2 on 2025-04-21 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0002_energybenchmark'),
    ]

    operations = [
        migrations.CreateModel(
            name='UtilityBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('utility_type', models.CharField(choices=[('Electricity', 'Electricity'), ('Water', 'Water'), ('Gas', 'Gas')], max_length=20)),
                ('billing_month', models.DateField()),
                ('units_consumed', models.FloatField()),
                ('cost_per_unit', models.FloatField()),
                ('total_amount', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
