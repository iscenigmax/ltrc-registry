# Generated by Django 2.1.3 on 2019-11-05 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w2r', '0004_auto_20191101_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='registro',
            name='confirmado',
            field=models.BooleanField(default=False, verbose_name='Acepto términos y condiciones'),
            preserve_default=False,
        ),
    ]
