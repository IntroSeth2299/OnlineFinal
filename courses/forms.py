from django import forms
from .models import Course
class CourseAddForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields ='__all__'