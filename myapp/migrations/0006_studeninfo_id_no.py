# Generated by Django 2.1.1 on 2018-10-13 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20181012_1034'),
    ]

    operations = [
        migrations.AddField(
            model_name='studeninfo',
            name='id_no',
            field=models.IntegerField(default=1, unique=True),
            preserve_default=False,
        ),
    ]