from django import forms
from .models import User
class UserAddForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields ='__all__'