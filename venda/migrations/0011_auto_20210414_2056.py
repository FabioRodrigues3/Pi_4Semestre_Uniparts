# Generated by Django 3.0.6 on 2021-04-14 23:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('venda', '0010_auto_20200701_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='cep',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='cpf',
        ),
        migrations.AddField(
            model_name='usuario',
            name='datanasc',
            field=models.DateField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Historia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('tipo_de_genero', models.CharField(choices=[('RO', 'Romance'), ('DR', 'Drama'), ('AV', 'Aventura'), ('TE', 'Terror')], default='AV', max_length=2)),
                ('classificacao', models.IntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=9)),
                ('descricao', models.TextField()),
                ('avaliacao', models.BooleanField(default=True)),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venda.Usuario')),
            ],
        ),
    ]
