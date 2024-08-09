from django.forms import ModelForm
from shopping_list.models import List
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm:
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',)

class ListForm(ModelForm):
    class Meta:
        model = List
        fields = "__all__"