# Generated by Django 4.2.1 on 2023-07-06 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_category_bid_buyer_bid_cur_bid_item_comment_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
