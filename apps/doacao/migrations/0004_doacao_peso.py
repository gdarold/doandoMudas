# Generated by Django 2.2.6 on 2020-08-05 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doacao', '0003_auto_20200804_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='doacao',
            name='peso',
            field=models.DecimalField(decimal_places=2, default=0.1, max_digits=4),
        ),
    ]
