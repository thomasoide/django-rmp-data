# Generated by Django 2.1.1 on 2018-10-05 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rmp', '0007_auto_20181005_2144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accchem',
            name='quantity_lbs',
            field=models.IntegerField(help_text='The amount of the substance released in the accident, in pounds, to two significant digits.', null=True, verbose_name='Amount Released (lbs)'),
        ),
        migrations.AlterField(
            model_name='tbls6accidentchemicals',
            name='quantity_lbs',
            field=models.DecimalField(decimal_places=1, help_text='The amount of the substance released in the accident, in pounds, to two significant digits.', max_digits=8, null=True, verbose_name='Amount Released (lbs)'),
        ),
    ]
