from django import forms
from .models import Employee
class EmployeeAddForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeEditForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields ='__all__'