# Generated by Django 3.2.6 on 2021-09-11 20:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0083_auto_20210911_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='data_criacao',
        ),
        migrations.RemoveField(
            model_name='item',
            name='observacoes',
        ),
        migrations.RemoveField(
            model_name='item',
            name='opcao',
        ),
        migrations.RemoveField(
            model_name='item',
            name='projeto',
        ),
        migrations.RemoveField(
            model_name='item',
            name='subitem',
        ),
    ]
