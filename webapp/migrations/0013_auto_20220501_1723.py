# Generated by Django 3.2.9 on 2022-05-01 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_alter_phelkayword_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phelkayword',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='zhebsaword',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
