# Generated by Django 2.2.6 on 2020-08-20 00:41

import apps.endereco.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0007_auto_20200819_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doacao',
            name='endereco',
            field=models.CharField(max_length=255, verbose_name=apps.endereco.models.Endereco),
        ),
    ]
