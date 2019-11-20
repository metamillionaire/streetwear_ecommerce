from django.views.generic import ListView
from .models  import Product
from . import views

class Home(ListView):
    model = Product
    template_name = 'products/home.html'

