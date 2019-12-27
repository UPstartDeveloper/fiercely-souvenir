# Generated by Django 3.0 on 2019-12-27 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0003_auto_20191227_1551'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='title',
            field=models.CharField(default='', help_text='Headline for review.', max_length=200, unique=True),
            preserve_default=False,
        ),
    ]
