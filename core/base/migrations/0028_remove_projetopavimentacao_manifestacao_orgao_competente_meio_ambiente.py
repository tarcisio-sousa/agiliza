# Generated by Django 3.1.3 on 2020-12-05 03:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0027_remove_projetopavimentacao_art'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetopavimentacao',
            name='manifestacao_orgao_competente_meio_ambiente',
        ),
    ]