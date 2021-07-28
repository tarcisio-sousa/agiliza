# Generated by Django 3.1.3 on 2021-07-20 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0046_projeto_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='projeto',
            field=models.ManyToManyField(blank=True, null=True, to='base.Projeto'),
        ),
        migrations.AddField(
            model_name='opcao',
            name='item',
            field=models.ManyToManyField(blank=True, null=True, to='base.Item'),
        ),
    ]