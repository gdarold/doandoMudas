# Generated by Django 2.2.6 on 2020-08-12 00:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_auto_20200811_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pessoa',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
