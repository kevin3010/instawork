# Generated by Django 4.2.8 on 2023-12-11 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammember',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('regular', 'regular')], max_length=10),
        ),
    ]
