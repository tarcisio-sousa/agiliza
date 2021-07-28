# Generated by Django 3.1.3 on 2021-07-24 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0054_auto_20210724_1941'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('sort_order',)},
        ),
        migrations.AddField(
            model_name='item',
            name='sort_order',
            field=models.PositiveIntegerField(blank=True, db_index=True, editable=False, null=True),
        ),
    ]
