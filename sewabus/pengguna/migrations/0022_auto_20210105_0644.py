# Generated by Django 2.2 on 2021-01-05 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0021_auto_20201225_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databus',
            name='ac',
            field=models.CharField(default=None, max_length=15),
        ),
    ]