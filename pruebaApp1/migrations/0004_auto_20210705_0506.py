# Generated by Django 3.2.4 on 2021-07-05 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pruebaApp1', '0003_auto_20210702_2137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='Publicado',
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pruebaApp1.categoria'),
        ),
    ]