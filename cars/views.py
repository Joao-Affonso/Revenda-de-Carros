from django.shortcuts import render, redirect
from django.http import HttpResponse
from cars.models import Car
from cars.forms import CarModelForm

def cars_view(request):
    cars = Car.objects.all().order_by('model_year')
    
    search = request.GET.get('search')
    
    if search:
        cars =  cars.filter(model__icontains=search).order_by('model_year')
    
    return render(
        request, 
        'cars.html',
        {'cars': cars}
        
    )
    
def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(request, 'new_car.html', {'new_car_form': new_car_form})
    