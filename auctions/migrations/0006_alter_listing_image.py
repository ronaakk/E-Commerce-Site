# Generated by Django 4.1.3 on 2023-01-10 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_alter_listing_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='https://user-images.githubusercontent.com/52632898/161646398-6d49eca9-267f-4eab-a5a7-6ba6069d21df.png', upload_to=''),
        ),
    ]
