# Generated by Django 4.2.4 on 2023-08-28 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_educacion_experiencia_investigacion_proyecto_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='tipo',
            field=models.IntegerField(),
        ),
    ]
