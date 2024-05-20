# Generated by Django 3.2.15 on 2024-04-12 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0117_execucaoconcedente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prefeitura',
            name='timbre',
            field=models.ImageField(blank=True, max_length=150, null=True, upload_to='uploads/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='protocolo',
            name='responsavel',
            field=models.CharField(blank=True, choices=[('agiliza', 'AGILIZA'), ('funasa', 'FUNASA'), ('prefeitura', 'PREFEITURA'), ('assessoria', 'ASSESSORIA'), ('gabinete_parlamentar', 'GABINETE_PARLAMENTAR'), ('orgao_convenente', 'ORGAO_CONVENENTE'), ('concedente', 'CONCEDENTE'), ('outros', 'OUTROS')], default=None, max_length=250, null=True),
        ),
    ]