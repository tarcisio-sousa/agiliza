# Generated by Django 3.1.3 on 2021-07-28 02:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0058_auto_20210726_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoAtiviade',
            fields=[
                ('protocolo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.protocolo')),
            ],
            bases=('base.protocolo',),
        ),
        migrations.CreateModel(
            name='LicenciamentoAmbiental',
            fields=[
                ('protocolo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.protocolo')),
            ],
            bases=('base.protocolo',),
        ),
        migrations.RemoveField(
            model_name='protocolo',
            name='arquivo',
        ),
        migrations.RemoveField(
            model_name='protocolo',
            name='descricao',
        ),
        migrations.AddField(
            model_name='protocolo',
            name='anexo',
            field=models.FileField(blank=True, max_length=150, null=True, upload_to='uploads/protocolos/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='protocolo',
            name='consideracoes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='protocolo',
            name='data_prevista',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Data Prevista'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='protocolo',
            name='situacao',
            field=models.CharField(blank=True, choices=[('enviado_analise', 'Enviado p/ análise'), ('solicitada_complementacao', 'Solicitada complementação'), ('aprovado', 'Aprovado')], default=None, max_length=150, null=True),
        ),
    ]
