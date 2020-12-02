# Generated by Django 3.1.3 on 2020-12-02 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_auto_20201202_0736'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=15)),
                ('descricao', models.CharField(max_length=200)),
                ('tipo_resposta', models.CharField(choices=[('checkbox', 'Check List'), ('radio', 'Opção'), ('text', 'Objetivo')], default='text', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='cargo',
            old_name='nome',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='orgao',
            old_name='nome',
            new_name='descricao',
        ),
        migrations.RenameField(
            model_name='prefeitura',
            old_name='secretario_de_obras',
            new_name='secretario_obras',
        ),
        migrations.CreateModel(
            name='Subitem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.item')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='projeto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='base.projeto'),
        ),
    ]
