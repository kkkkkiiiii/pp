# Generated by Django 3.2.18 on 2023-06-14 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20230614_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='ccc',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='cc',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
