# Generated by Django 2.2 on 2020-12-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0020_auto_20201225_0253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kabupaten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='biaya',
            name='provinsi_asal',
        ),
        migrations.RemoveField(
            model_name='biaya',
            name='provinsi_tujuan',
        ),
        migrations.AlterField(
            model_name='biaya',
            name='kabupaten_asal',
            field=models.CharField(choices=[('Sleman', 'Sleman'), ('Kulon_Progo', 'KulonProgo')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='biaya',
            name='kabupaten_tujuan',
            field=models.CharField(choices=[('Sleman', 'Sleman'), ('Kulon_Progo', 'KulonProgo')], default=None, max_length=100, null=True),
        ),
    ]