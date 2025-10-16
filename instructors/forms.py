from django import forms
from .models import Instructor
class InstructorAddForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

class InstructorEditForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields ='__all__'