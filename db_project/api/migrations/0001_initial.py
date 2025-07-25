# Generated by Django 5.2.4 on 2025-07-19 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.type')),
            ],
        ),
    ]
