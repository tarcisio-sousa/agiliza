# Generated by Django 3.1.3 on 2021-01-11 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0040_auto_20210110_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='convenio',
            name='arquivo_extrato',
            field=models.FileField(blank=True, max_length=150, null=True, upload_to='uploads/%Y/%m/%d'),
        ),
    ]