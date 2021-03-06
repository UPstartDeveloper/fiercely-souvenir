# Generated by Django 3.0 on 2019-12-28 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airlines', '0005_auto_20191227_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='price',
            field=models.DecimalField(decimal_places=2, help_text='How much did you pay this airline? Please leave out currency symbols (i.e. $).', max_digits=9),
        ),
    ]
