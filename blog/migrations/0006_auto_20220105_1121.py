# Generated by Django 2.2.12 on 2022-01-05 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20220105_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]