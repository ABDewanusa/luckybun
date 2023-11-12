from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="homepage"),
    path("", views.home, name="home"),
]
