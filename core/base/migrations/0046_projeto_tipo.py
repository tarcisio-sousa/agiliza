# Generated by Django 3.1.3 on 2021-07-20 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0045_remove_projeto_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='tipo',
            field=models.CharField(blank=True, choices=[('estrada', 'Estrada'), ('equipamento', 'Equipamento'), ('praca', 'Praca'), ('pavimentacao', 'Pavimentacao'), ('centro_esportivo', 'Centro Esportivo'), ('edificacao', 'Edificação')], default=None, max_length=150, null=True),
        ),
    ]
