# Generated by Django 2.1.3 on 2019-11-28 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0012_auto_20191128_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corredor',
            name='guia',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
