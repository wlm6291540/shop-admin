# Generated by Django 3.0.4 on 2020-03-26 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0011_auto_20200325_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
    ]
