# Generated by Django 3.0.5 on 2020-04-15 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0009_remove_branches_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='branches',
            name='id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
