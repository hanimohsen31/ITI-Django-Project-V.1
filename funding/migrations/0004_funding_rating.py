# Generated by Django 3.0.7 on 2021-12-04 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0003_auto_20211203_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='funding',
            name='rating',
            field=models.FloatField(default=0, null=True),
        ),
    ]