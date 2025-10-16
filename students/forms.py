from django import forms
from .models import Student
class StudentAddForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class StudentEditForm(forms.ModelForm):
    class Meta:
        model = Student
        fields ='__all__'