from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from .models import Post


# Create your views here.
def home(request):
    return HttpResponse("hello world!")


class HomeView(ListView):
    model = Post
    template_name = "index.html"
