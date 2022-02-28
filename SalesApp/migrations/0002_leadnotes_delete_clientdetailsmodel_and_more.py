# Generated by Django 4.0 on 2022-02-17 12:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SalesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeadNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_comment', models.TextField(blank=True, null=True)),
                ('next_followup', models.CharField(blank=True, max_length=120, null=True)),
                ('is_demo', models.IntegerField()),
                ('is_site_visit', models.IntegerField()),
                ('is_electric_layout', models.IntegerField()),
                ('is_proposal', models.IntegerField()),
                ('is_lead_conform', models.IntegerField()),
                ('discount', models.CharField(blank=True, max_length=20, null=True)),
                ('lead_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leaddetails', to='SalesApp.leadmodel')),
            ],
            options={
                'db_table': 'lead_notes',
            },
        ),
        migrations.DeleteModel(
            name='ClientDetailsModel',
        ),
        migrations.DeleteModel(
            name='SkromanClients',
        ),
    ]
