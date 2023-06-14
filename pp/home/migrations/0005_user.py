# Generated by Django 3.2.18 on 2023-06-14 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20230614_0926'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
