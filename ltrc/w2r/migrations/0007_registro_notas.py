# Generated by Django 2.1.3 on 2019-11-09 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w2r', '0006_auto_20191104_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='notas',
            field=models.TextField(blank=True, null=True),
        ),
    ]
