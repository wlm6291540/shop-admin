# Generated by Django 3.0.4 on 2020-03-25 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0010_auto_20200325_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=255, verbose_name='菜单名'),
        ),
    ]