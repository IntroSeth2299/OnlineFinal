from django import forms
from .models import Tag
class TagAddForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = '__all__'

class TagEditForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields ='__all__'