# Generated by Django 5.1 on 2024-08-29 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cursos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('plataforma', models.CharField(max_length=100)),
                ('instituição', models.CharField(max_length=100)),
                ('imagem', models.ImageField(upload_to='cursos/')),
            ],
        ),
        migrations.CreateModel(
            name='Habilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('descrição', models.TextField()),
                ('imagem', models.ImageField(upload_to='habilidades/')),
            ],
        ),
    ]
