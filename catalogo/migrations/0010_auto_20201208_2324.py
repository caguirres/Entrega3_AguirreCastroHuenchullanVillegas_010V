# Generated by Django 3.1.3 on 2020-12-09 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0009_auto_20201208_2317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id_usuario',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
    ]