# Generated by Django 3.2.5 on 2021-08-08 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0074_delete_edificacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projeto',
            name='convenio',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='orgao',
        ),
        migrations.RemoveField(
            model_name='projetocontrole',
            name='alternativa',
        ),
        migrations.RemoveField(
            model_name='projetocontrole',
            name='comentario',
        ),
        migrations.RemoveField(
            model_name='projetocontrole',
            name='data_prevista',
        ),
        migrations.RemoveField(
            model_name='projetocontrole',
            name='item',
        ),
        migrations.RemoveField(
            model_name='projetocontrole',
            name='observacoes',
        ),
        migrations.RemoveField(
            model_name='projetocontrole',
            name='responsavel',
        ),
        migrations.AddField(
            model_name='projetocontrole',
            name='convenio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.convenio'),
        ),
        migrations.AddField(
            model_name='projetocontrole',
            name='orgao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.orgao'),
        ),
        migrations.CreateModel(
            name='ProjetoControleItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('comentario', models.CharField(blank=True, max_length=250, null=True)),
                ('data_prevista', models.DateField(blank=True, null=True, verbose_name='Data Prevista')),
                ('alternativa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.alternativa')),
                ('controle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.projetocontrole')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.item')),
                ('responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.responsavel')),
            ],
        ),
    ]
