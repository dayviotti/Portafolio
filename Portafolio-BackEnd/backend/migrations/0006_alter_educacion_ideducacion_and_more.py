# Generated by Django 4.2.5 on 2023-09-08 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_redsocial_persona_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educacion',
            name='idEducacion',
            field=models.AutoField(max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='experiencia',
            name='idExperiencia',
            field=models.AutoField(max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='investigacion',
            name='idInvestigacion',
            field=models.AutoField(max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='persona',
            name='id',
            field=models.AutoField(max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='idProyecto',
            field=models.AutoField(max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='redsocial',
            name='idRedSocial',
            field=models.AutoField(max_length=2, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='skill',
            name='idSkill',
            field=models.AutoField(max_length=2, primary_key=True, serialize=False),
        ),
    ]
