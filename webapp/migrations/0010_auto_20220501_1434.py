# Generated by Django 3.2.9 on 2022-05-01 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_auto_20220501_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phelkayword',
            name='p_phrase',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='zhebsaword',
            name='z_phrase',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
