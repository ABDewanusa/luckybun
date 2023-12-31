from django.contrib import admin

from .models import *

# Register all models for the admin interface
admin.site.register(InventoryItems)
admin.site.register(Products)
admin.site.register(Production)
admin.site.register(ProductItems)
admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(Shipments)
admin.site.register(ShipmentItems)
admin.site.register(ProductReturns)
admin.site.register(Accounts)
admin.site.register(Transactions)
admin.site.register(Sales)
admin.site.register(Refunds)
admin.site.register(Expenses)
admin.site.register(Employees)
admin.site.register(Salaries)
admin.site.register(Purchases)
