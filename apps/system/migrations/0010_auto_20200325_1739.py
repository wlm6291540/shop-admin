# Generated by Django 3.0.4 on 2020-03-25 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0009_auto_20200325_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='desc',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='备注'),
        ),
    ]
