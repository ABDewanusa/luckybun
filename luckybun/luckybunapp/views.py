from django.views import View
from django.shortcuts import render
from .models import *


# Create your views here.
class Dashboard(View):
    name = "Dashboard"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class Orders(View):
    name = "Orders"
    context = {"title": name, "orders": Orders.objects.all()}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class Shipments(View):
    name = "Shipments"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class Returns(View):
    name = "Returns"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class Customers(View):
    name = "Customers"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class Products(View):
    name = "Products"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class Ingredients(View):
    name = "Ingredients"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class Inventory(View):
    name = "Inventory"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class Accounting(View):
    name = "Accounting"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)


class Settings(View):
    name = "Settings"
    context = {"title": name}

    def get(self, request):
        return render(request, f"pages/{self.name}.html", self.context)
