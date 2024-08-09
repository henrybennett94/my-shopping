from django.shortcuts import render, get_object_or_404, reverse
from django.views.generic import TemplateView
from django.views.generic import ListView
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .models import List
from .forms import ListForm

# Create your views here.
class HomePage(TemplateView):
    """
    Displays home page
    """
    template_name='index.html'

@login_required
class ShoppingListView(ListView):
    queryset = List.objects.all()
    template_name = "list_view.html"

@login_required
def create_shopping_list(request):
    """
    #Allows user to open a blank list and add items
    """
    user = request.user
    if request.method == 'POST':
        list_form = ListForm(request.POST)
        if list_form.is_valid():
            shopping_list = list_form.save(commit=False)
            shopping_list.user = request.user
            shopping_list.save()
            return redirect('list_view', id=shopping_list.id)
    
    list_form = ListForm()

    return render(request, 'lists/new_list.html', {'list_form': list_form})
    
@login_required
def list_view(request):
    """
    #Displays previously created lists as clickable to open
    """
    lists = List.objects.all()
    return render(request, 'lists/my_lists.html', {'lists': lists})

def edit(request, slug, list_id):
    """
    view to edit lists
    """
    if request.method == "POST":
        queryset = List.objects.all()
        list = get_object_or_404(queryset, slug=slug)
        list_form = ListForm(data=request.POST, instance=list)

        if list_form.is_valid():
            list = list_form.save(commit=False)
            list.approved = False
            list.save()
            messages.add_message(request, messages.SUCCESS, 'List Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating list!')
        
        return HttpResponseRedirect(reverse('list_view', args=[slug]))

