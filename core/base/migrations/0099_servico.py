# Generated by Django 3.2.9 on 2022-01-07 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0098_auto_20211209_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objeto', models.CharField(blank=True, max_length=150, null=True)),
                ('observacoes', models.TextField(blank=True, null=True)),
                ('data_cadastro', models.DateField(auto_now=True, verbose_name='Data de Cadastro')),
                ('data_prevista', models.DateField(blank=True, null=True, verbose_name='Data Prevista')),
                ('status', models.BooleanField(default=True)),
                ('prefeitura', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.prefeitura')),
                ('responsavel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.responsavel')),
            ],
            options={
                'verbose_name': 'serviço',
                'verbose_name_plural': 'serviços',
            },
        ),
    ]
