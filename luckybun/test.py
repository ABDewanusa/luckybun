import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "luckybun.settings.base")
import django

django.setup()
from luckybunapp.models import *

from datetime import date

# today = date.today()
# print(str(today) + )


# c1 = Customer.objects.get(CustomerID=1)
# c2 = Customer.objects.get(CustomerID=2)
# p1 = Product.objects.get(ProductID=1)
# p2 = Product.objects.get(ProductID=2)
# o1 = Orders.objects.get(OrderID=1)
# o2 = Orders.objects.get(OrderID=2)
# o3 = Orders.objects.get(OrderID=3)
# o4 = Orders.objects.get(OrderID=4)

# oi = OrderItems.objects.filter(OrderID=4, ProductID=2)
# oi.Quantity = 10
# oi.save()

# print(list(oi) == [])
# oi = OrderItems(OrderID=o4, ProductID=p1, Quantity=10)
# oi.save()

# revOrders = Orders.objects.all().order_by("-OrderID")
# for order in revOrders:
#     print(order)
transaction = Transactions.objects.get(TransactionID=1)
print(transaction.Description)
