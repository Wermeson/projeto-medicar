# Generated by Django 3.2.7 on 2021-09-14 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='consulta',
            old_name='data',
            new_name='data_agendamento',
        ),
    ]
