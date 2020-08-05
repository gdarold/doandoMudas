# Generated by Django 2.2.6 on 2020-08-05 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tipo_planta', '0001_initial'),
        ('tipo_doacao', '0001_initial'),
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField()),
                ('custo', models.DecimalField(decimal_places=2, default=1, max_digits=4)),
                ('status', models.BooleanField(default=True)),
                ('doador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pessoa.Pessoa')),
                ('tipo_doacao', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tipo_doacao.Tipo_doacao')),
                ('tipo_planta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='tipo_planta.Tipo_planta')),
            ],
        ),
    ]
