# Generated by Django 5.1.1 on 2024-09-14 18:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0003_produto_atualizado_em_produto_criado_em'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfilusuario',
            name='endereco',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_usuario', to='estoque.endereco'),
        ),
        migrations.AlterField(
            model_name='perfilusuario',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_usuario', to=settings.AUTH_USER_MODEL),
        ),
    ]
