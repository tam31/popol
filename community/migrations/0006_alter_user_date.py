# Generated by Django 4.0.3 on 2022-05-24 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0005_alter_user_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.IntegerField(null=True),
        ),
    ]
