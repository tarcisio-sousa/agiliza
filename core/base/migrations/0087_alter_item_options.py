# Generated by Django 3.2.6 on 2021-09-16 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0086_item_sort_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('sort_order',), 'verbose_name_plural': 'itens'},
        ),
    ]
