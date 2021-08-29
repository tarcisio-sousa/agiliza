# Generated by Django 3.2.6 on 2021-08-19 03:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0076_projetocontrole_projeto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opcao',
            options={'verbose_name': 'opção', 'verbose_name_plural': 'opções'},
        ),
        migrations.AlterModelOptions(
            name='projetocontrole',
            options={'verbose_name': 'controle', 'verbose_name_plural': 'controles'},
        ),
        migrations.AlterModelOptions(
            name='projetocontroleitem',
            options={'verbose_name': 'itens'},
        ),
        migrations.AddField(
            model_name='alternativa',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='cargo',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='convenio',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='item',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='itemalternativa',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='opcao',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='orgao',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='profissional',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='projeto',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='projetocontrole',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='projetocontroleitem',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='proposta',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='protocolo',
            name='data_criacao',
            field=models.DateField(auto_now=True, verbose_name='Data de Criação'),
        ),
        migrations.AddField(
            model_name='protocolo',
            name='data_protocolado',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data Protocolado'),
            preserve_default=False,
        ),
    ]