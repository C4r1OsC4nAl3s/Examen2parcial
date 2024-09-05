# Generated by Django 5.0.6 on 2024-07-06 21:09

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Service title', max_length=80)),
                ('description', models.CharField(default='Service Description', max_length=120)),
                ('type', models.CharField(choices=[('APP', 'Aplication'), ('APM', 'Movil Aplication'), ('SRV', 'Servers')], max_length=4)),
                ('created_at', models.DateField(blank=True, default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='activities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='title', max_length=80)),
                ('description', models.CharField(default='description', max_length=250)),
                ('created_at', models.DateField(blank=True, default=datetime.date.today)),
                ('due_date', models.DateField(blank=True, default=datetime.date.today)),
                ('status', models.CharField(choices=[('DONE', 'Finished'), ('PEND', 'Pending'), ('UNDO', 'Unodone')], max_length=4)),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
