# Generated by Django 4.1.3 on 2023-01-25 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0019_listing_last_bid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=35),
        ),
    ]
