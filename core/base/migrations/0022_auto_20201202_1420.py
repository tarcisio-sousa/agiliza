# Generated by Django 3.1.3 on 2020-12-02 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_auto_20201202_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resposta',
            name='tipo',
            field=models.CharField(choices=[('text', 'Texto'), ('checkbox', 'Check'), ('radio', 'Radio')], default='text', max_length=150),
        ),
    ]
