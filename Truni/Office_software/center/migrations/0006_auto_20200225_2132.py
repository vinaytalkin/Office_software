# Generated by Django 2.0 on 2020-02-25 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('center', '0005_registration_agreeterms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='father_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='registration',
            name='spouse_name',
            field=models.CharField(max_length=100),
        ),
    ]
