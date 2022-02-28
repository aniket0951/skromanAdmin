# Generated by Django 4.0 on 2022-02-17 12:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('SalesApp', '0002_leadnotes_delete_clientdetailsmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='leadnotes',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='leadnotes',
            name='uptime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
