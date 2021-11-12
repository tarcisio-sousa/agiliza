# Generated by Django 3.2.9 on 2021-11-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0090_rename_numero_convenio_convenio_numero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='convenio',
            name='valor',
        ),
        migrations.RemoveField(
            model_name='convenio',
            name='valor_repasse',
        ),
        migrations.AddField(
            model_name='proposta',
            name='valor_convenio',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, null=True, verbose_name='Valor do convênio'),
        ),
        migrations.AddField(
            model_name='proposta',
            name='valor_repasse',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=19, null=True, verbose_name='Valor do repasse'),
        ),
    ]
