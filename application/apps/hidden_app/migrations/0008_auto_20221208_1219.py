# Generated by Django 3.2.15 on 2022-12-08 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hidden_app', '0007_additionalinformation'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='latitude',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='широта'),
        ),
        migrations.AddField(
            model_name='info',
            name='longitude',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='долгота'),
        ),
    ]