# Generated by Django 2.2 on 2021-01-05 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0022_auto_20210105_0644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='databus',
            name='bagasi',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='databus',
            name='bantal',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='databus',
            name='dvd',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='databus',
            name='sabuk_pengaman',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='databus',
            name='selimut',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='databus',
            name='smoking_area',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='databus',
            name='stop_kontak',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='databus',
            name='toilet',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='databus',
            name='tv',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='databus',
            name='wifi',
            field=models.CharField(default=None, max_length=15),
        ),
    ]
