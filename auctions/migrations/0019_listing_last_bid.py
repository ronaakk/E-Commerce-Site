# Generated by Django 4.1.3 on 2023-01-20 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0018_listing_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='last_bid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.bid'),
        ),
    ]
