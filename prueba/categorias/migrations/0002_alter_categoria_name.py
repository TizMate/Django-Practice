# Generated by Django 4.1.5 on 2023-01-31 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
