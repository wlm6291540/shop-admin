# Generated by Django 3.0.4 on 2020-03-25 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0008_menu_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='menus',
            field=models.ManyToManyField(null=True, to='system.Menu', verbose_name='关联菜单'),
        ),
    ]
