from django.urls import path
from . import views

urlpatterns = [
    path("", views.viewDashboard.as_view(), name="Dashboard"),
    path("orders/", views.viewOrders.as_view(), name="Orders"),
    path("orderscreate/", views.viewOrdersCreate.as_view(), name="OrdersCreate"),
    path("ordersdetail/", views.viewOrdersDetail.as_view(), name="OrdersDetail"),
    path("ordersedit/", views.viewOrdersEdit.as_view(), name="OrdersEdit"),
    path("shipments/", views.viewShipments.as_view(), name="Shipments"),
    path("returns/", views.viewReturns.as_view(), name="Returns"),
    path("customers/", views.viewCustomers.as_view(), name="Customers"),
    path("products/", views.viewProducts.as_view(), name="Products"),
    path("ingredients/", views.viewIngredients.as_view(), name="Ingredients"),
    path("inventory/", views.viewInventory.as_view(), name="Inventory"),
    path("accounting/", views.viewAccounting.as_view(), name="Accounting"),
    path("transactions/", views.viewTransactions.as_view(), name="Transactions"),
    path(
        "transactionscreate/",
        views.viewTransactionsCreate.as_view(),
        name="TransactionsCreate",
    ),
    path("settings/", views.viewSettings.as_view(), name="Settings"),
]
