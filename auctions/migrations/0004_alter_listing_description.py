# Generated by Django 4.1.3 on 2023-01-08 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_listing_category_alter_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.CharField(blank=True, max_length=1064, null=True),
        ),
    ]
