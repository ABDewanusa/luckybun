from django.views.generic import ListView
from .models import Post


# Create your views here.
class dashboard(ListView):
    model = Post
    template_name = "index.html"
