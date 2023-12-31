from django.views import View
from django.shortcuts import render
from .models import *
from datetime import date

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
class viewDashboard(View):
    name = "Dashboard"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class viewOrders(View):
    context = {
        "title": "Orders",
    }

    def post(self, request):
        if "deleteOrder" in request.POST.keys():
            OrderID = request.POST["OrderID"]
            Order = Orders.objects.get(OrderID=OrderID)
            Order.delete()
        self.context["revOrders"] = Orders.objects.all().order_by("-OrderID")
        return render(request, f"pages/Orders/Orders.html", self.context)

    def get(self, request):
        self.context["revOrders"] = Orders.objects.all().order_by("-OrderID")
        return render(request, f"pages/Orders/Orders.html", self.context)


class viewOrdersCreate(View):
    context = {
        "title": "Orders Create",
        "rev_orders": Orders.objects.all().order_by("-OrderID"),
    }

    def get(self, request):
        latestOrder = list(Orders.objects.all().order_by("-OrderID"))[0]
        self.context["newOrderID"] = latestOrder.OrderID + 1
        self.context["Customers"] = Customers.objects.all()

        self.context["Statuses"] = ["Pending", "Processing", "Shipped"]
        self.context["PaymentStatuses"] = ["Unpaid", "Paid"]

        return render(request, f"pages/Orders/OrdersCreate.html", self.context)


class viewOrdersDetail(View):
    context = {
        "title": "Order Detail",
    }

    def post(self, request):
        if "ProcessOrder" in request.POST.keys():
            order = Orders.objects.get(OrderID=request.POST["OrderID"])
            order.Status = "Processing"
            order.save()

        self.context["OrderID"] = request.POST["OrderID"]
        self.context["Order"] = Orders.objects.get(OrderID=request.POST["OrderID"])
        self.context["OrderItems"] = OrderItems.objects.filter(
            OrderID=request.POST["OrderID"]
        )

        if self.context["Order"].PaymentStatus == "Unpaid":
            self.context["PayDetails"] = []
            self.context["Total"] = 0
            for orderitem in self.context["OrderItems"]:
                subtotal = orderitem.Quantity * orderitem.ProductID.Price
                self.context["Total"] += subtotal
                PayDetail = {
                    "name": orderitem.ProductID.Name,
                    "description": orderitem.ProductID.Description,
                    "quantity": orderitem.Quantity,
                    "price": orderitem.ProductID.Price,
                    "subtotal": subtotal,
                }
                self.context["PayDetails"].append(PayDetail)
            pass

        return render(request, f"pages/Orders/OrdersDetail.html", self.context)


class viewOrdersEdit(View):
    context = {
        "title": "Order Edit",
    }

    def post(self, request):
        OrderID = ""
        if "createOrder" in request.POST.keys():
            OrderID = request.POST["newOrderID"]
            Cust = Customers.objects.get(CustomerID=request.POST["selectedCustomerID"])
            Order = Orders(
                OrderID=OrderID,
                CustomerID=Cust,
                OrderDate=request.POST["selectedDate"],
                Status=request.POST["newStatus"],
                PaymentStatus=request.POST["newPaymentStatus"],
            )
            Order.save()
        else:
            OrderID = request.POST["OrderID"]

            if "changeStatus" in request.POST.keys():
                newStatus = request.POST["newStatus"]
                Order = Orders.objects.get(OrderID=OrderID)
                Order.Status = newStatus
                Order.save()

            elif "changePaymentStatus" in request.POST.keys():
                newPaymentStatus = request.POST["newPaymentStatus"]
                Order = Orders.objects.get(OrderID=OrderID)
                Order.PaymentStatus = newPaymentStatus
                Order.save()

            elif "changeItemQuantity" in request.POST.keys():
                if request.POST["newItemQuantity"] != "":
                    ProductID = request.POST["ProductID"]
                    OrderItem = OrderItems.objects.get(
                        OrderID=OrderID, ProductID=ProductID
                    )
                    OrderItem.Quantity = request.POST["newItemQuantity"]
                    OrderItem.save()

            elif "deleteItem" in request.POST.keys():
                ProductID = request.POST["ProductID"]
                OrderItem = OrderItems.objects.get(OrderID=OrderID, ProductID=ProductID)
                OrderItem.delete()

            elif "addOrderItem" in request.POST.keys():
                if (
                    request.POST["newItemQuantity"] != ""
                    and request.POST["ProductID"] != ""
                ):
                    newItemQuantity = int(request.POST["newItemQuantity"])
                    ProductID = request.POST["ProductID"]
                    que = OrderItems.objects.filter(
                        OrderID=OrderID, ProductID=ProductID
                    )
                    if list(que) == []:
                        newOrderItem = OrderItems(
                            OrderID=Orders.objects.get(OrderID=OrderID),
                            ProductID=Products.objects.get(ProductID=ProductID),
                            Quantity=newItemQuantity,
                        )
                        newOrderItem.save()
                    else:
                        newOrderItem = OrderItems(
                            OrderID=Orders.objects.get(OrderID=OrderID),
                            ProductID=Products.objects.get(ProductID=ProductID),
                        )
                        for oi in que:
                            newItemQuantity += oi.Quantity
                            oi.delete()
                        newOrderItem.Quantity = newItemQuantity
                        newOrderItem.save()

        self.context["OrderID"] = OrderID
        self.context["Order"] = Orders.objects.get(OrderID=OrderID)
        self.context["OrderItems"] = OrderItems.objects.filter(OrderID=OrderID)
        self.context["Status"] = self.context["Order"].Status
        self.context["Statuses"] = ["Pending", "Processing", "Shipped"]
        self.context["PaymentStatus"] = self.context["Order"].PaymentStatus
        self.context["PaymentStatuses"] = ["Unpaid", "Paid"]
        self.context["Products"] = Products.objects.all()

        return render(request, f"pages/Orders/OrdersEdit.html", self.context)


class viewShipments(View):
    name = "Shipments"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class viewReturns(View):
    name = "Returns"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class viewCustomers(View):
    name = "Customers"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class viewProducts(View):
    name = "Products"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class viewIngredients(View):
    name = "Ingredients"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class viewInventory(View):
    name = "Inventory"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class viewAccounting(View):
    name = "Accounting"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/Accounting/{self.name}.html", self.context)


class viewTransactions(View):
    context = {"title": "Transactions"}

    def get(self, request):
        self.context["AccountID"] = 1
        self.context["Accounts"] = Accounts.objects.all()
        self.context["Transactions"] = Transactions.objects.filter(
            AccountID=self.context["AccountID"]
        )
        return render(request, f"pages/Accounting/transactions.html", self.context)

    def post(self, request):
        if "createTransaction" in request.POST.keys():
            AccountID = Accounts.objects.get(AccountID=int(request.POST["AccountID"]))
            transaction = Transactions(
                TransactionID=request.POST["newTransactionID"],
                TransactionDate=request.POST["TransactionDate"],
                TransactionType=request.POST["TransactionType"],
                Description=request.POST["Description"],
                AccountID=AccountID,
            )
            if request.POST["TransactionType"] == "Debit":
                transaction.Amount = (-1) * float(request.POST["Amount"])
            else:
                transaction.Amount = float(request.POST["Amount"])

            transaction.save()

        if "deleteTransaction" in request.POST.keys():
            transaction = Transactions.objects.get(
                TransactionID=int(request.POST["TransactionID"])
            )
            transaction.delete()

        self.context["AccountID"] = int(request.POST["AccountID"])
        self.context["Accounts"] = Accounts.objects.all()
        self.context["revTransactions"] = Transactions.objects.filter(
            AccountID=self.context["AccountID"]
        ).order_by("-TransactionID")
        TotalAmount = sum(
            [
                float(transaction.Amount)
                for transaction in self.context["revTransactions"]
            ]
        )
        self.context["TotalAmount"] = "Rp {:,.2f}".format(TotalAmount)

        return render(request, f"pages/Accounting/Transactions.html", self.context)


class viewTransactionsCreate(View):
    context = {"title": "New Transaction"}

    def post(self, request):
        latestTransaction = list(Transactions.objects.all().order_by("-TransactionID"))[
            0
        ]
        self.context["newTransactionID"] = latestTransaction.TransactionID + 1
        self.context["Account"] = Accounts.objects.get(
            AccountID=request.POST["AccountID"]
        )
        self.context["Accounts"] = Accounts.objects.all()
        return render(
            request, f"pages/Accounting/TransactionsCreate.html", self.context
        )


class viewSettings(View):
    name = "Settings"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)
