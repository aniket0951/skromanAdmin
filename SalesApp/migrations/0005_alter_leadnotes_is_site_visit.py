# Generated by Django 4.0 on 2022-02-23 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SalesApp', '0004_alter_leadnotes_is_demo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leadnotes',
            name='is_site_visit',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
