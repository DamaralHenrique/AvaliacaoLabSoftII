# Generated by Django 5.0.1 on 2024-04-17 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingresso_app', '0002_estadio_usuario_rename_lugar_ingresso_vaga_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresso',
            name='cliente',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
