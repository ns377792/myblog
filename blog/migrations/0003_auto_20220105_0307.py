# Generated by Django 2.2.12 on 2022-01-05 03:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220105_0306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='main_image',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='heading',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=models.CharField(max_length=450),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='featured_post',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.CharField(max_length=100),
        ),
    ]