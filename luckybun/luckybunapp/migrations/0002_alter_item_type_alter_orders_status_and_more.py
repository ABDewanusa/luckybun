# Generated by Django 4.2.7 on 2023-11-12 01:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("luckybunapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="Type",
            field=models.CharField(
                choices=[
                    ("inventory", "Inventory"),
                    ("ingredient", "Ingredient"),
                    ("tool", "Tool"),
                ],
                default="ingredient",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="orders",
            name="Status",
            field=models.CharField(
                choices=[
                    ("processing", "Processing"),
                    ("shipped", "Shipped"),
                    ("completed", "Completed"),
                    ("pending", "Pending"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="status",
            field=models.CharField(
                choices=[("published", "Published"), ("draft", "Draft")],
                default="draft",
                max_length=10,
            ),
        ),
        migrations.AlterField(
            model_name="shipment",
            name="ShipmentStatus",
            field=models.CharField(
                choices=[("complete", "Complete"), ("partial", "Partial")],
                default="partial",
                max_length=20,
            ),
        ),
    ]
