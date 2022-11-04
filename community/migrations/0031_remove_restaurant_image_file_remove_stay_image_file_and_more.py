# Generated by Django 4.0.3 on 2022-09-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0030_alter_restaurant_visitcnt_alter_stay_visitcnt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='image_file',
        ),
        migrations.RemoveField(
            model_name='stay',
            name='image_file',
        ),
        migrations.AlterField(
            model_name='tour',
            name='visitCnt',
            field=models.IntegerField(default=0),
        ),
    ]
