# Generated by Django 2.0.6 on 2018-06-13 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0013_person_news_opt_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='news_opt_in',
            field=models.BooleanField(default=True),
        ),
    ]
