# Generated by Django 3.2.9 on 2022-04-30 12:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_auto_20220430_1815'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactdetails',
            name='contact_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]