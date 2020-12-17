# Generated by Django 3.1.3 on 2020-12-15 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_remove_projetopavimentacao_manifestacao_orgao_competente_meio_ambiente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pavimentacao',
            fields=[
                ('projeto_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.projeto')),
                ('sr', models.CharField(blank=True, max_length=250, null=True)),
                ('numero_contrato', models.CharField(blank=True, max_length=250, null=True)),
                ('data_assinatura', models.CharField(blank=True, max_length=250, null=True)),
                ('programa', models.CharField(blank=True, max_length=250, null=True)),
                ('modalidade', models.CharField(blank=True, max_length=250, null=True)),
                ('proponente', models.CharField(blank=True, max_length=250, null=True)),
                ('tipo_proponente', models.CharField(blank=True, max_length=250, null=True)),
                ('empreendimento', models.CharField(blank=True, max_length=250, null=True)),
                ('localizacao', models.CharField(blank=True, max_length=250, null=True)),
                ('objetivo_pleito', models.CharField(blank=True, max_length=250, null=True)),
                ('copia_plano_trabalho', models.CharField(blank=True, max_length=250, null=True)),
                ('qci', models.CharField(blank=True, max_length=250, null=True)),
                ('planta_georreferenciada', models.CharField(blank=True, max_length=250, null=True)),
                ('projeto_geometrico_planta_baixa', models.CharField(blank=True, max_length=250, null=True)),
                ('projeto_geometrico_perfil_longitudinal', models.CharField(blank=True, max_length=250, null=True)),
                ('projeto_terraplenagem_notas_servico', models.CharField(blank=True, max_length=250, null=True)),
                ('projeto_terraplenagem_relatorio_volumes', models.CharField(blank=True, max_length=250, null=True)),
                ('projeto_terraplenagem_secoes_transversais', models.CharField(blank=True, max_length=250, null=True)),
                ('projeto_pavimentacao_secao_tipo', models.CharField(blank=True, max_length=250, null=True)),
                ('projeto_drenagem', models.CharField(blank=True, max_length=250, null=True)),
                ('projeto_sinalizacao_viaria', models.CharField(blank=True, max_length=250, null=True)),
                ('projeto_calcadas_acessibilidade', models.CharField(blank=True, max_length=250, null=True)),
                ('memorial_descritivo_projeto', models.CharField(blank=True, max_length=250, null=True)),
                ('especificacoes_tecnicas', models.CharField(blank=True, max_length=250, null=True)),
                ('orcamentos_detalhados', models.CharField(blank=True, max_length=250, null=True)),
                ('composicoes_custos_unitarios', models.CharField(blank=True, max_length=250, null=True)),
                ('detalhamento_bdi', models.CharField(blank=True, max_length=250, null=True)),
                ('cronograma_fisico_financeiro_empreendimento', models.CharField(blank=True, max_length=250, null=True)),
                ('memoria_calculo_dimensionamento', models.CharField(blank=True, max_length=250, null=True)),
                ('declaracao_bem_uso_comum_povo', models.CharField(blank=True, max_length=250, null=True)),
                ('art_projeto', models.CharField(blank=True, max_length=250, null=True)),
                ('art_orcamento', models.CharField(blank=True, max_length=250, null=True)),
                ('art_acessibilidade', models.CharField(blank=True, max_length=250, null=True)),
                ('declaracao_munutencao_conservacao', models.CharField(blank=True, max_length=250, null=True)),
                ('declaracao_existencia_rede_abastecimento_agua', models.CharField(blank=True, max_length=250, null=True)),
                ('declaracao_existencia_solucao_esgotamento_sanitario', models.CharField(blank=True, max_length=250, null=True)),
                ('declaracao_regime_execucao_obra', models.CharField(blank=True, max_length=250, null=True)),
                ('equipe_coordenacao_projeto', models.CharField(blank=True, max_length=250, null=True)),
                ('contrato_elaboracao_projeto_engenharia', models.CharField(blank=True, max_length=250, null=True)),
                ('declaracao_autor_projeto_sinalizacao', models.CharField(blank=True, max_length=250, null=True)),
                ('relatorio_fotografico', models.CharField(blank=True, max_length=250, null=True)),
                ('servico_apto_para_analise_tecnica', models.CharField(blank=True, max_length=250, null=True)),
                ('comentario_analise_tecnica', models.CharField(blank=True, max_length=250, null=True)),
                ('servico_terceirizado', models.CharField(blank=True, max_length=250, null=True)),
                ('justificativa_comentarios', models.CharField(blank=True, max_length=250, null=True)),
                ('atividade', models.CharField(blank=True, max_length=250, null=True)),
                ('produto', models.CharField(blank=True, max_length=250, null=True)),
                ('linha', models.CharField(blank=True, max_length=250, null=True)),
                ('fonte', models.CharField(blank=True, max_length=250, null=True)),
                ('responsavel_verificacao', models.CharField(blank=True, max_length=250, null=True)),
                ('data', models.CharField(blank=True, max_length=250, null=True)),
                ('local_data', models.CharField(blank=True, max_length=250, null=True)),
                ('responsavel_tecnico', models.CharField(blank=True, max_length=250, null=True)),
                ('matricula', models.CharField(blank=True, max_length=250, null=True)),
                ('cpf', models.CharField(blank=True, max_length=250, null=True)),
                ('crea', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name': 'projeto de pavimentação',
                'verbose_name_plural': 'projetos de pavimentação',
            },
            bases=('base.projeto',),
        ),
        migrations.DeleteModel(
            name='ProjetoPavimentacao',
        ),
        migrations.RemoveField(
            model_name='projeto',
            name='descricao',
        ),
        migrations.AddField(
            model_name='projeto',
            name='convenio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='base.convenio'),
        ),
    ]
