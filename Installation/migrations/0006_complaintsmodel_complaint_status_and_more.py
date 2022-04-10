# Generated by Django 4.0 on 2022-04-05 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
        ('Installation', '0005_complaintsmodel_remove_skromanclients_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaintsmodel',
            name='complaint_status',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='ComplaintAssignModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('uptime', models.DateTimeField(auto_now=True)),
                ('complaint_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaint', to='Installation.complaintsmodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee', to='AdminApp.users')),
            ],
            options={
                'db_table': 'complaint_assign',
            },
        ),
        migrations.CreateModel(
            name='AssignedUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctime', models.DateTimeField(auto_now_add=True)),
                ('uptime', models.DateTimeField(auto_now=True)),
                ('complaint_assign_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='complaint_assigned', to='Installation.complaintassignmodel')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignee_user', to='AdminApp.users')),
            ],
            options={
                'db_table': 'assigned_users',
            },
        ),
    ]