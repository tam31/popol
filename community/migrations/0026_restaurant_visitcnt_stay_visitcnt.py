# Generated by Django 4.0.4 on 2022-07-13 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0025_remove_input_mbti_remove_tour_mbti_delete_mbti'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='visitCnt',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stay',
            name='visitCnt',
            field=models.IntegerField(null=True),
        ),
    ]
