# Generated by Django 3.2.12 on 2022-04-06 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0102_alter_proposta_lei_complementar'),
    ]

    operations = [
        migrations.AddField(
            model_name='convenio',
            name='agencia',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='convenio',
            name='banco',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='convenio',
            name='conta',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
