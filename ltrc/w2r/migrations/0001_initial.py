# Generated by Django 2.1.3 on 2019-10-21 02:43

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_final', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'proyecto',
                'verbose_name_plural': 'proyectos',
            },
        ),
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=300)),
                ('apellido_paterno', models.CharField(max_length=300)),
                ('apellido_materno', models.CharField(max_length=300)),
                ('edad', models.PositiveSmallIntegerField()),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('objetivo_5k', models.PositiveSmallIntegerField(choices=[(1, '15 a 20 minutos'), (2, '21 a 25 minutos'), (3, '26 a 30 minutos'), (4, '31 a 35 minutos'), (5, '+35 minutos')])),
                ('tiempo_5k', models.TimeField(blank=True)),
                ('tiempo_10k', models.TimeField(blank=True)),
                ('tiempo_15k', models.TimeField(blank=True)),
                ('tiempo_21k', models.TimeField(blank=True)),
                ('tiempo_42k', models.TimeField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('proyecto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='proyecto_registro_objects', to='w2r.Proyecto')),
            ],
            options={
                'verbose_name': 'registro',
                'verbose_name_plural': 'registros',
            },
        ),
    ]
