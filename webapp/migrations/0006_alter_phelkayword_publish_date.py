# Generated by Django 3.2.9 on 2022-04-27 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_rename_zhebsa_pronunciation_zhebsaword_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phelkayword',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
