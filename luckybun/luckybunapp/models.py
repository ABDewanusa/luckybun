from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Item(models.Model):
    options = {
        ("ingredient", "Ingredient"),
        ("tool", "Tool"),
        ("inventory", "Inventory"),
    }

    ItemID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Type = models.CharField(max_length=20, choices=options, default="ingredient")
    Quantity = models.IntegerField()


class Product(models.Model):
    ProductID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    StockQuantity = models.IntegerField()


class Production(models.Model):
    ProductionID = models.IntegerField(primary_key=True)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    QuantityProduced = models.IntegerField()
    ProductionDate = models.DateField()
    ExpirationDate = models.DateField()


class ProductItems(models.Model):
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    ItemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    RequiredQuantity = models.IntegerField(primary_key=True)


class Customer(models.Model):
    CustomerID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    Contact = models.CharField(max_length=255)
    Location = models.CharField(max_length=255)
    Notes = models.TextField()


class Orders(models.Model):
    status_opt = {
        ("pending", "Pending"),
        ("processing", "Processing"),
        ("shipped", "Shipped"),
        ("completed", "Completed"),
    }

    PaymentStatus_opt = {("unpaid", "Unpaid"), ("paid", "Paid")}

    Status = models.CharField(max_length=20, choices=status_opt, default="pending")
    PaymentStatus = models.CharField(
        max_length=20, choices=PaymentStatus_opt, default="unpaid"
    )
    OrderID = models.IntegerField(primary_key=True)
    OrderDate = models.DateField()
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)


class OrderItems(models.Model):
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    Quantity = models.IntegerField(primary_key=True)


class Shipment(models.Model):
    options = {
        ("partial", "Partial"),
        ("complete", "Complete"),
    }

    ShipmentStatus = models.CharField(max_length=20, choices=options, default="partial")
    ShipmentID = models.IntegerField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)


class ShipmentItems(models.Model):
    ShipmentID = models.ForeignKey(Shipment, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    ProductionID = models.ForeignKey(Production, on_delete=models.CASCADE, default="")
    QuantityShipped = models.IntegerField(primary_key=True)
    ShipmentDate = models.DateField()


class ProductReturn(models.Model):
    ReturnID = models.IntegerField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Product, on_delete=models.CASCADE)
    ReturnDate = models.DateField()
    ReturnReason = models.CharField(max_length=255)
    QuantityReturned = models.IntegerField()
    ProductionID = models.ForeignKey(Production, on_delete=models.CASCADE)


class Account(models.Model):
    AccountID = models.IntegerField(primary_key=True)
    AccountName = models.CharField(max_length=255)


class SalesTransaction(models.Model):
    SaleID = models.IntegerField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    TransactionDate = models.DateField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    AccountID = models.ForeignKey(Account, on_delete=models.CASCADE)


class RefundTransaction(models.Model):
    RefundTransactionID = models.IntegerField(primary_key=True)
    CustomerID = models.ForeignKey(Customer, on_delete=models.CASCADE)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    TransactionDate = models.DateField()
    RefundAmount = models.DecimalField(max_digits=10, decimal_places=2)
    AccountID = models.ForeignKey(Account, on_delete=models.CASCADE)


class ExpenseTransaction(models.Model):
    ExpenseID = models.IntegerField(primary_key=True)
    TransactionDate = models.DateField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField()
    AccountID = models.ForeignKey(Account, on_delete=models.CASCADE)


class Employee(models.Model):
    EmployeeID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=255)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)


class SalaryTransaction(models.Model):
    SalaryID = models.IntegerField(primary_key=True)
    EmployeeID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    TransactionDate = models.DateField()
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    AccountID = models.ForeignKey(Account, on_delete=models.CASCADE)


class ItemPurchase(models.Model):
    PurchaseID = models.IntegerField(primary_key=True)
    ItemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    PurchaseDate = models.DateField()
    ExpirationDate = models.DateField()
    AmountPaid = models.DecimalField(max_digits=10, decimal_places=2)
    ExpenseID = models.ForeignKey(ExpenseTransaction, on_delete=models.CASCADE)


class Post(models.Model):
    options = {
        ("draft", "Draft"),
        ("published", "Published"),
    }

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=options, default="draft")

    class Meta:
        ordering = ("created_at",)

    def __str__(self):
        return self.title
