# Generated by Django 4.2.1 on 2023-07-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_bid_prevbid_bid_prevbuyer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(blank=True, choices=[('others', 'others'), ('Books', 'Books'), ('Art', 'Art'), ('Electronics', 'Electronics'), ('Fashon', 'Fashon'), ('Appliances', 'Appliances')], max_length=20, null=True),
        ),
    ]