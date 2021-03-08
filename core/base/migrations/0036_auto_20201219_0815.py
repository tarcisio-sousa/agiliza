# Generated by Django 3.1.3 on 2020-12-19 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0035_edificacao'),
    ]

    operations = [
        migrations.AddField(
            model_name='edificacao',
            name='anotacao_responsabilidade_tecnica_art',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='aprovacao_projetos_orgaos_competentes',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='arquitetura',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='art_acessibilidade',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='art_execucao',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='art_fiscalizacao',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='art_orcamento',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='art_projeto_arquitetonico',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='art_projeto_combate_incendio_spda',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='art_projeto_instalacoes_eletricas',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='art_projeto_instalacoes_hidrosanitarias',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='composicoes_custos_unitarios',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='copia_plano_trabalho',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='cronograma_fisico_financeiro',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='cronograma_fisico_financeiro_individual',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='declaracao_dominio_publico',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='declaracao_manutencao_conservacao',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='declaracao_viabilidade_atendimento_rede_esgosto',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='declaracao_viabilidade_coleta_lixo',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='declaracao_viabilidade_fornecimento_agua',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='declaracao_viabilidade_fornecimento_energia',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='declaracoes_orgaos_competentes',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='detalhamento_bdi',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='dispensa_licenciamento',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='elemento_descritivo_projeto_basico',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='especificacoes_tecnicas',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='existem_obras_iniciadas',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='levantamento_topografico_area_intervencao',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='licenca_instalacao',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='licenca_operacao',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='licenca_previa',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='manifestacao_orgao_meio_ambiente',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='matricula_certidao_terreno_registro_imoveis',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='memoria_calculo_dimensionamento',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='memorial_descritivo',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='opcao_compra_venda_terreno',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='orcamentos_detalhados',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='planta_localizacao_empreendimento',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='projeto_acessibilidade',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='projeto_estrutural',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='projeto_instalacoes_aguas_pluviais',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='projeto_instalacoes_combate_incendio_panico',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='projeto_instalacoes_eletricas',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='projeto_instalacoes_hidraulicas',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='projeto_instalacoes_logica_telefonicas',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='projeto_instalacoes_sanitarias',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='projeto_sistema_prevencao_descargas_atmosfericas',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='projeto_tecnico_pecas_graficas',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='qci',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='relatorio_sondagem',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='termo_doacao',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='teste_absorcao_percolacao_terreno',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='edificacao',
            name='valores_investimento',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]