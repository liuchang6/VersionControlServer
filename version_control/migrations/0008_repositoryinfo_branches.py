# Generated by Django 3.0.2 on 2020-02-01 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('version_control', '0007_auto_20200131_1718'),
    ]

    operations = [
        migrations.AddField(
            model_name='repositoryinfo',
            name='branches',
            field=models.CharField(default='dev', max_length=100, verbose_name='代码分支'),
            preserve_default=False,
        ),
    ]
