# Generated by Django 4.1.3 on 2023-01-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_alter_listing_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, choices=[('Toys', 'Toys'), ('Electronics', 'Electronics'), ('Lifestyle', 'Lifestyle'), ('Home', 'Home'), ('Fashion', 'Fashion'), ('Other', 'Other')], max_length=64),
        ),
    ]