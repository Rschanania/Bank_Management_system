# Generated by Django 3.0.5 on 2020-04-11 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0004_auto_20200411_0652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bank',
            old_name='id',
            new_name='bank_id',
        ),
        migrations.RenameField(
            model_name='bank',
            old_name='name',
            new_name='bank_name',
        ),
    ]
