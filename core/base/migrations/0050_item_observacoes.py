# Generated by Django 3.1.3 on 2021-07-24 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0049_auto_20210720_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='observacoes',
            field=models.TextField(blank=True, null=True),
        ),
    ]
