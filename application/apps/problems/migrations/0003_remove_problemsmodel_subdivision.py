# Generated by Django 3.2.15 on 2022-12-07 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0002_problemsmodel_subdivision'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problemsmodel',
            name='subdivision',
        ),
    ]