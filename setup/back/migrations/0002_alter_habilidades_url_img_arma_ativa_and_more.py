# Generated by Django 4.0.6 on 2022-08-04 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habilidades',
            name='url_img_arma_ativa',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='habilidades',
            name='url_img_dois_ativa',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='habilidades',
            name='url_img_passiva_ativa',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='habilidades',
            name='url_img_um_ativa',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AlterField(
            model_name='personagem',
            name='descricao_odio',
            field=models.CharField(blank=True, max_length=666),
        ),
        migrations.AlterField(
            model_name='personagem',
            name='url_img_risadola',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]