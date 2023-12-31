from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class InventoryItems(models.Model):
    options = {
        ("Ingredient", "Ingredient"),
        ("Tool", "Tool"),
        ("Inventory", "Inventory"),
    }

    ItemID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Type = models.CharField(max_length=20, choices=options, default="ingredient")
    Quantity = models.IntegerField()


class Products(models.Model):
    ProductID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    StockQuantity = models.IntegerField()


class Production(models.Model):
    ProductionID = models.AutoField(primary_key=True)
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    QuantityProduced = models.IntegerField()
    ProductionDate = models.DateField()
    ExpirationDate = models.DateField()


class ProductItems(models.Model):
    ProductID = models.AutoField(primary_key=True)
    InventoryItemID = models.ForeignKey(InventoryItems, on_delete=models.CASCADE)
    RequiredQuantity = models.IntegerField()


class Customers(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    models.IntegerField(primary_key=True, auto_created=True)
    Name = models.CharField(max_length=255)
    Contact = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    Notes = models.TextField()


class StyleVariants(models.Model):
    StyleId = models.AutoField(primary_key=True)
    label = models.CharField(max_length=255)
    variant = models.CharField(max_length=255)


class Orders(models.Model):
    status_opt = {
        ("Pending", "Pending"),
        ("Processing", "Processing"),
        ("Shipped", "Shipped"),
        ("Completed", "Completed"),
    }

    PaymentStatus_opt = {("Unpaid", "Unpaid"), ("Paid", "Paid")}

    OrderID = models.AutoField(primary_key=True)
    Status = models.CharField(max_length=20, choices=status_opt, default="Pending")
    PaymentStatus = models.CharField(
        max_length=20, choices=PaymentStatus_opt, default="Unpaid"
    )
    OrderDate = models.DateField()
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)


class OrderItems(models.Model):
    OrderItemId = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField()


class Shipments(models.Model):
    options = {
        ("Partial", "Partial"),
        ("Complete", "Complete"),
    }

    ShipmentID = models.AutoField(primary_key=True)
    ShipmentStatus = models.CharField(max_length=20, choices=options, default="Partial")
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)


class ShipmentItems(models.Model):
    ShipmentItemsID = models.AutoField(primary_key=True)
    ShipmentID = models.ForeignKey(Shipments, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    ProductionID = models.ForeignKey(Production, on_delete=models.CASCADE, default="")
    QuantityShipped = models.IntegerField()
    ShipmentDate = models.DateField()


class ProductReturns(models.Model):
    ReturnID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    ReturnDate = models.DateField()
    ReturnReason = models.CharField(max_length=255)
    QuantityReturned = models.IntegerField()
    ProductionID = models.ForeignKey(Production, on_delete=models.CASCADE)


class Accounts(models.Model):
    AccountID = models.AutoField(primary_key=True)
    AccountName = models.CharField(max_length=255)


class Transactions(models.Model):
    type_opt = {
        ("Credit", "Credit"),
        ("Debit", "Debit"),
    }

    TransactionID = models.AutoField(primary_key=True)
    TransactionDate = models.DateField()
    TransactionType = models.CharField(
        max_length=20, choices=type_opt, default="Credit"
    )
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    AccountID = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    Description = models.TextField()


class Sales(models.Model):
    SaleID = models.AutoField(primary_key=True)
    TransactionID = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)


class Refunds(models.Model):
    RefundID = models.AutoField(primary_key=True)
    TransactionID = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)


class RefundItems(models.Model):
    RefundItemID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField()


class Expenses(models.Model):
    ExpenseID = models.AutoField(primary_key=True)
    TransactionID = models.ForeignKey(Transactions, on_delete=models.CASCADE)
    Description = models.TextField()


class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)


class Salaries(models.Model):
    SalaryID = models.AutoField(primary_key=True)
    EmployeeID = models.ForeignKey(Employees, on_delete=models.CASCADE)
    TransactionID = models.ForeignKey(Transactions, on_delete=models.CASCADE)


class Purchases(models.Model):
    PurchaseID = models.AutoField(primary_key=True)
    InventoryItemID = models.ForeignKey(InventoryItems, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    ExpenseID = models.ForeignKey(Expenses, on_delete=models.CASCADE)
