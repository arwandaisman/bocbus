# Generated by Django 2.2 on 2021-01-07 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0032_auto_20210107_0809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ketersediaan',
            old_name='id_bus',
            new_name='sedia',
        ),
    ]
