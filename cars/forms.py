from django import forms
from cars.models import  Car

    
class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
def clean_value(self):
    value = self.cleanned_data.get('value')
    if value < 20000:
        self.add_error('value', 'O valor mínimo do carro deve ser de R$ 15.000')
    return value

def clean_factory_year(self):
    factory_year = self.cleanned_data.get('factory_year')
    if factory_year < 1975:
        self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 1975')
    return factory_year
        
        

