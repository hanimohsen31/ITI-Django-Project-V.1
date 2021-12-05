# Generated by Django 3.2.9 on 2021-12-05 16:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('funding', '0006_alter_funding_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_donations',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Project_donations', to='funding.funding'),
        ),
        migrations.AlterField(
            model_name='project_donations',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Project_donations', to=settings.AUTH_USER_MODEL),
        ),
    ]
