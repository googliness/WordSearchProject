# Generated by Django 2.2.6 on 2019-10-23 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wordtuple',
            name='freq',
            field=models.IntegerField(),
        ),
    ]
