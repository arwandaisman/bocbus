# Generated by Django 2.2 on 2021-01-07 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0027_ketersediaan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biaya',
            name='nama',
        ),
        migrations.DeleteModel(
            name='Hotel',
        ),
        migrations.DeleteModel(
            name='Kabupaten',
        ),
        migrations.DeleteModel(
            name='Biaya',
        ),
    ]
