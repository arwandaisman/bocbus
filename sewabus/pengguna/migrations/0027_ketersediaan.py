# Generated by Django 2.2 on 2021-01-07 04:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0026_remove_databus_no_plat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ketersediaan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_mulai', models.DateField(default=None)),
                ('tanggal_selesai', models.DateField(default=None)),
                ('nama_penyewa', models.CharField(default=None, max_length=50)),
                ('no_hp_penyewa', models.CharField(default=None, max_length=50)),
                ('nik', models.CharField(default=None, max_length=50)),
                ('sedia', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='sedia', to='pengguna.DataBus')),
            ],
        ),
    ]