# Generated by Django 2.0.6 on 2018-07-18 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0012_auto_20180718_1302'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mealstoorder',
            old_name='meal',
            new_name='meals',
        ),
        migrations.RenameField(
            model_name='mealstoorder',
            old_name='order',
            new_name='orders',
        ),
        migrations.RenameField(
            model_name='servicepercentage',
            old_name='percentage',
            new_name='percentages',
        ),
        migrations.RemoveField(
            model_name='order',
            name='totalsum',
        ),
        migrations.AddField(
            model_name='check',
            name='totalsum',
            field=models.FloatField(null=True),
        ),
    ]
