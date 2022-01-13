# Generated by Django 3.2.8 on 2021-12-26 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shorturl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin_url', models.URLField()),
                ('short_query', models.CharField(max_length=8)),
                ('visits', models.IntegerField(default=0)),
            ],
        ),
    ]
