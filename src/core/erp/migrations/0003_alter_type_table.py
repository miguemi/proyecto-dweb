# Generated by Django 4.1 on 2022-08-27 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_type_employee_type'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='type',
            table='empleado_tipo',
        ),
    ]
