# Generated by Django 3.2.6 on 2021-08-29 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0078_alter_proposta_valor_contrapartida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetocontroleitem',
            name='alternativa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.alternativa'),
        ),
    ]
