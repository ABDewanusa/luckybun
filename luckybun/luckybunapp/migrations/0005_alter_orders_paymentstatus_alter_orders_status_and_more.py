# Generated by Django 4.2.7 on 2023-11-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("luckybunapp", "0004_orders_paymentstatus_alter_item_type_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="orders",
            name="PaymentStatus",
            field=models.CharField(
                choices=[("unpaid", "Unpaid"), ("paid", "Paid")],
                default="unpaid",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="orders",
            name="Status",
            field=models.CharField(
                choices=[
                    ("shipped", "Shipped"),
                    ("completed", "Completed"),
                    ("processing", "Processing"),
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
                choices=[("partial", "Partial"), ("complete", "Complete")],
                default="partial",
                max_length=20,
            ),
        ),
    ]
