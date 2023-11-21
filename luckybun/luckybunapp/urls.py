from django.urls import path
from . import views

urlpatterns = [
    path("", views.Dashboard.as_view(), name="Dashboard"),
    path("Orders/", views.Orders.as_view(), name="Orders"),
    path("Shipments/", views.Shipments.as_view(), name="Shipments"),
    path("Returns/", views.Returns.as_view(), name="Returns"),
    path("Customers/", views.Customers.as_view(), name="Customers"),
    path("Products/", views.Products.as_view(), name="Products"),
    path("Ingredients/", views.Ingredients.as_view(), name="Ingredients"),
    path("Inventory/", views.Inventory.as_view(), name="Inventory"),
    path("Accounting/", views.Accounting.as_view(), name="Accounting"),
    path("Settings/", views.Settings.as_view(), name="Settings"),
]
