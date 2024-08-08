from django.shortcuts import render
from django.views.generic import TemplateView
from .models import List

# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name='index.html'

class ShoppingListView(generic.ListView):
    queryset = List.objects.all()
    template_name = "list_view.html"