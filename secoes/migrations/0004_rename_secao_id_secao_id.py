# Generated by Django 5.1 on 2024-09-01 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secoes', '0003_rename_id_secao_secao_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='secao',
            old_name='secao_id',
            new_name='id',
        ),
    ]
