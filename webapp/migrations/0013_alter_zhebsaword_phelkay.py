# Generated by Django 3.2.9 on 2022-05-03 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0012_alter_phelkayword_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zhebsaword',
            name='phelkay',
            field=models.ManyToManyField(related_name='zhesa', to='webapp.PhelkayWord'),
        ),
    ]