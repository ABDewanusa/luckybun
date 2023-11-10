from django.contrib import admin

from .models import *

# Register all models for the admin interface
admin.site.register(Item)
admin.site.register(Product)
admin.site.register(Production)
admin.site.register(ProductItems)
admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(OrderItems)
admin.site.register(Shipment)
admin.site.register(ShipmentItems)
admin.site.register(ProductReturn)
admin.site.register(Account)
admin.site.register(SalesTransaction)
admin.site.register(RefundTransaction)
admin.site.register(ExpenseTransaction)
admin.site.register(Employee)
admin.site.register(SalaryTransaction)
admin.site.register(ItemPurchase)