# Generated by Django 3.0.5 on 2020-04-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0006_auto_20200411_1140'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='branches',
            name='id',
        ),
        migrations.AlterField(
            model_name='branches',
            name='ifsc',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
