# Generated by Django 3.2.6 on 2021-09-11 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0082_auto_20210911_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name_plural': 'itens'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='sort_order',
        ),
    ]
