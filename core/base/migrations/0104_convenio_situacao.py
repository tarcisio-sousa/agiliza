# Generated by Django 3.2.12 on 2022-04-24 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0103_auto_20220406_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='convenio',
            name='situacao',
            field=models.CharField(blank=True, choices=[('aguardando-aprovacao', 'AGUARDANDO APROVAÇÃO DO PROJETO'), ('projeto-aprovado', 'PROJETO APROVADO'), ('aguardando-licitacao', 'AGUARDANDO LICITAÇÃO'), ('aguardando-aceite-licitacao', 'AGUARDANDO ACEITE DA LICITAÇÃO'), ('licitacao-aprovada', 'LICITAÇÃO APROVADA, AGUARDANDO RECURSO'), ('recurs-em-conta', 'RECURSO EM CONTA'), ('em-execucao', 'EM EXECUÇÃO'), ('convenio-concluido', 'CONVENIO CONCLUÍDO'), ('prestacao-de-contas-concluida', 'PRESTAÇÃO DE CONTAS CONCLUÍDA')], default='aguardando-aprovacao', max_length=50, null=True),
        ),
    ]
