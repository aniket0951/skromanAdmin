# Generated by Django 4.0 on 2022-02-09 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=210, null=True)),
                ('email', models.CharField(blank=True, max_length=120, null=True)),
                ('password', models.CharField(blank=True, max_length=120, null=True)),
                ('user_dept', models.CharField(blank=True, max_length=120, null=True)),
                ('designation', models.CharField(blank=True, max_length=120, null=True)),
                ('work', models.CharField(blank=True, max_length=120, null=True)),
                ('is_active', models.IntegerField()),
            ],
            options={
                'db_table': 'skroman_users',
            },
        ),
    ]
