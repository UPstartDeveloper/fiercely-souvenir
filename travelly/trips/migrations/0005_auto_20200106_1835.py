# Generated by Django 3.0 on 2020-01-06 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0004_auto_20200106_1433'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='terminal',
        ),
        migrations.AddField(
            model_name='trip',
            name='airline',
            field=models.CharField(blank=True, help_text='Which airline are you flying with?', max_length=600),
        ),
        migrations.AddField(
            model_name='trip',
            name='depart_from',
            field=models.CharField(blank=True, help_text='Which airport are you boarding from?', max_length=600),
        ),
    ]
