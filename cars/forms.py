from django import forms
from cars.models import Brand, Car

# class CarForm(forms.Form):
#   model = forms.CharField(max_length=200)
#   brand = forms.ModelChoiceField(Brand.objects.all())
#   factory_year = forms.IntegerField()
#   model_year = forms.IntegerField()
#   plate = forms.CharField(max_length=10)
#   value = forms.FloatField()
#   photo = forms.ImageField()

#   def save(self):
#     car = Car(
#       model = self.cleaned_data['model'],
#       brand = self.cleaned_data['brand'],
#       factory_year = self.cleaned_data['factory_year'],
#       model_year = self.cleaned_data['model_year'],
#       plate = self.cleaned_data['plate'],
#       value = self.cleaned_data['value'],
#       photo = self.cleaned_data['photo'],
#     )

#     car.save()

#     return car
  

class CarModelForm(forms.ModelForm):
  class Meta:
    model = Car
    fields = '__all__'

  def clean_value(self):
    value = self.cleaned_data.get('value')

    if value < 20000:
      self.add_error('value', 'Min value must be 20000')
    
    return value
  
  def clean_factory_year(self):
    factory_year = self.cleaned_data.get('factory_year')

    if factory_year < 1975:
      self.add_error('factory_year', 'Too old car')
    
    return factory_year