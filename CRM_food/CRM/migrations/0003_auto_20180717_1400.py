# Generated by Django 2.0.6 on 2018-07-17 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0002_auto_20180717_0059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='isitopen',
            new_name='is_it_open',
        ),
        migrations.AddField(
            model_name='order',
            name='meals',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Order', to='CRM.Meal'),
        ),
    ]