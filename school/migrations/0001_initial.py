# Generated by Django 2.1.1 on 2018-10-12 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('district', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('stablished_date', models.DateTimeField()),
            ],
        ),
    ]
