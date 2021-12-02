# Generated by Django 3.2.9 on 2021-12-02 00:37

from django.db import migrations, models
import django.db.models.deletion
import funding.models


class Migration(migrations.Migration):

    dependencies = [
        ('funding', '0003_auto_20211202_0237'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_pics',
            name='pic',
            field=models.ImageField(default=1, upload_to=funding.models.get_image_name, verbose_name='Project Image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project_pics',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funding.funding'),
        ),
        migrations.AddField(
            model_name='project_tags',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funding.funding'),
        ),
        migrations.AddField(
            model_name='project_tags',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='funding.tags'),
        ),
        migrations.AlterUniqueTogether(
            name='project_tags',
            unique_together={('tag', 'project')},
        ),
    ]
