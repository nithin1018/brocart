# Generated by Django 5.1.4 on 2025-01-12 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="total_price",
            field=models.FloatField(default=0.0),
        ),
    ]
