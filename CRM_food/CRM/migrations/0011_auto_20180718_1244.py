# Generated by Django 2.0.6 on 2018-07-18 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CRM', '0010_auto_20180718_1235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='role',
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Order', to='CRM.User'),
        ),
    ]
