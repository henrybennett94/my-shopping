from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('<slug: slug>/edit/<int:list_id>', views.edit, name='edit'),
]