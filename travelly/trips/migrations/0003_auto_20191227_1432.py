# Generated by Django 3.0 on 2019-12-27 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0002_auto_20191225_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='slug',
            field=models.CharField(blank=True, editable=False, help_text='Unique URL path to access this trip.Computer Generated.', max_length=600),
        ),
    ]
