# Generated by Django 3.2.9 on 2022-05-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0010_auto_20220501_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zhebsaword',
            name='publish_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
