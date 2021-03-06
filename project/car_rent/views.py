from django.shortcuts import render, redirect
from django.views.generic import View
from . import forms, models


# Create your views here.
class CarView(View):
    template_name = 'car_rent/car.html'

    def get(self, request):
        form = forms.CarForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = forms.CarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, self.template_name, {'form': form})


class CarsListView(View):
    def get(self, request):
        cars = models.Car.objects.all()
        return render(request, 'car_rent/list.html', {'cars': cars})


class GaragesView(View):
    def get(self, request):
        garages = models.Garage.objects.all()
        return render(request, 'car_rent/garage.html', {'garages': garages})
