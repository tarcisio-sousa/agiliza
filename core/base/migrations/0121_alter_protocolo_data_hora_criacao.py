# Generated by Django 3.2.15 on 2024-04-13 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0120_protocolo_data_hora_criacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protocolo',
            name='data_hora_criacao',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Data hora de criação'),
        ),
    ]
