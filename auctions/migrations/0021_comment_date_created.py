# Generated by Django 4.1.3 on 2023-01-25 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0020_alter_listing_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
