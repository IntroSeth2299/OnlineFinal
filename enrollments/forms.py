from django import forms
from .models import Enrollment,LessonProgress,Review
class EnrollmentAddForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = '__all__'

class EnrollmentEditForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields ='__all__'

class LessonProgressAddForm(forms.ModelForm):
    class Meta:
        model = LessonProgress
        fields = '__all__'

class LessonProgressEditForm(forms.ModelForm):
    class Meta:
        model = LessonProgress
        fields ='__all__' 
class ReviewAddForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewEditForm(forms.ModelForm):
    class Meta:
        model = Review
        fields ='__all__'