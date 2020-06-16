from django.urls import path
from . import views

urlpatterns = [path('', views.CarView.as_view(), name='car'),
               path('list', views.CarsListView.as_view(), name='list')]