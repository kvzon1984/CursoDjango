# Generated by Django 3.2.9 on 2021-11-10 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='habilidad')),
            ],
            options={
                'verbose_name': 'Habilidad',
                'verbose_name_plural': 'Habilidades Empleados',
            },
        ),
        migrations.AlterModelOptions(
            name='empleados',
            options={'verbose_name': 'Mis Empleado', 'verbose_name_plural': 'Mis Empleados'},
        ),
    ]
