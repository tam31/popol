# Generated by Django 4.0.3 on 2022-08-22 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0029_remove_schedule_restaurant_remove_schedule_stay_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='visitCnt',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='stay',
            name='visitCnt',
            field=models.IntegerField(default=0),
        ),
    ]
