# Generated by Django 2.2.7 on 2019-12-21 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_ppm', '0010_auto_20191221_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coreip',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
        migrations.AlterField(
            model_name='internetip',
            name='ip',
            field=models.GenericIPAddressField(null=True),
        ),
    ]
