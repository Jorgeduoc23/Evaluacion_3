# Generated by Django 4.1.5 on 2023-01-30 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='macota',
            name='imagen',
            field=models.ImageField(null=True, upload_to='mascotas'),
        ),
    ]
