# Generated by Django 2.1.1 on 2018-09-29 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudenInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('roll', models.IntegerField(unique=True)),
                ('std_class', models.IntegerField()),
                ('gender', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=50)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
