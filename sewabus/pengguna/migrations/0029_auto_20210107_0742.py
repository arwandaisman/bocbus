# Generated by Django 2.2 on 2021-01-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0028_auto_20210107_0430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ketersediaan',
            name='sedia',
            field=models.CharField(max_length=50, null=True),
        ),
    ]