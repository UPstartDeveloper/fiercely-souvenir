# Generated by Django 3.0 on 2020-01-06 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0003_auto_20191227_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='arrive_at',
            field=models.CharField(blank=True, help_text='Which airport are you flying to?', max_length=600),
        ),
    ]
