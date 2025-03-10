# Generated by Django 5.1.4 on 2024-12-18 16:37

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tur nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Gul nomi')),
                ('description', models.TextField(blank=True, verbose_name='Tavsif')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flowers', to='gullar.type', verbose_name='Turi')),
            ],
        ),
    ]
