# Generated by Django 2.1.3 on 2019-11-01 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('w2r', '0003_auto_20191031_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registro',
            old_name='altura',
            new_name='estatura',
        ),
    ]
