
from django.urls import path
from . import views

from .views import HomePageView, SearchResultsView

urlpatterns = [
    #path('', views.home, name="home"),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home'),
    path('add', views.add, name="add"),
    path('edit/<list_id>', views.edit, name="edit"),  
    path('delete/<list_id>', views.delete, name="delete"), 
]
