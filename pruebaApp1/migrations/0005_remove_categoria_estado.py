# Generated by Django 3.2.4 on 2021-07-05 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pruebaApp1', '0004_auto_20210705_0506'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='estado',
        ),
    ]
