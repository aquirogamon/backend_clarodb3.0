# Generated by Django 2.2.7 on 2019-12-20 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_ppm', '0005_internetinterface_bpstime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internetinterface',
            name='bpsTime',
            field=models.DateTimeField(null=True, verbose_name='Fecha'),
        ),
    ]
