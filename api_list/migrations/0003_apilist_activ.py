# Generated by Django 3.2.9 on 2021-11-26 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_list', '0002_alter_apilist_api_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='apilist',
            name='activ',
            field=models.BooleanField(default=False),
        ),
    ]