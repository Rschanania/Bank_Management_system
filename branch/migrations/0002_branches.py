# Generated by Django 3.0.5 on 2020-04-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ifsc', models.CharField(max_length=20)),
                ('bank_id', models.IntegerField()),
                ('branch', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
    ]
