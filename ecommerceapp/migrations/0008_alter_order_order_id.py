# Generated by Django 4.1.5 on 2023-04-27 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0007_rename_orders_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
