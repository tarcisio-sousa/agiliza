# Generated by Django 3.2.12 on 2022-04-05 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0101_alter_projetocontroleitem_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposta',
            name='lei_complementar',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
