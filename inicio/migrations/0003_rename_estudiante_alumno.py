# Generated by Django 5.0.6 on 2024-06-13 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_auto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Estudiante',
            new_name='Alumno',
        ),
    ]