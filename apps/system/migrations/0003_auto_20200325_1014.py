# Generated by Django 3.0.4 on 2020-03-25 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_auto_20200325_1014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.Menu', verbose_name='父菜单'),
        ),
    ]
