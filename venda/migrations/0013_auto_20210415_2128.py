# Generated by Django 3.0.6 on 2021-04-16 00:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('venda', '0012_historia_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historia',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='historia',
            name='imagem',
            field=models.ImageField(default=False, upload_to='historia'),
        ),
    ]
