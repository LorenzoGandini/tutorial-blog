# Generated by Django 4.0.2 on 2022-02-24 11:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_delete_date_alter_post_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='delete_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 6, 11, 44, 53, 646958, tzinfo=utc)),
        ),
    ]
