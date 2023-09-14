# Generated by Django 4.2.5 on 2023-09-08 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_skill_porcentaje'),
    ]

    operations = [
        migrations.CreateModel(
            name='RedSocial',
            fields=[
                ('idRedSocial', models.CharField(max_length=1, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=150)),
                ('logo', models.ImageField(upload_to='imagenes/')),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='imagen',
            field=models.ImageField(default=0, upload_to='imagenes/'),
            preserve_default=False,
        ),
    ]