# Generated by Django 2.0 on 2020-02-12 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicmod',
            name='body',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basicmod',
            name='category',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
