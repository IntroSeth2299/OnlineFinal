from django import forms
from .models import Lesson
class LessonAddForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = '__all__'

class LessonEditForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields ='__all__'