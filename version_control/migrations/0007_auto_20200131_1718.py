# Generated by Django 3.0.2 on 2020-01-31 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version_control', '0006_auto_20200131_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositoryinfo',
            name='url',
            field=models.CharField(max_length=255, verbose_name='仓库地址'),
        ),
    ]