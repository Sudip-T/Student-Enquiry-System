from django import forms
from .models import CourseModel


class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = '__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'code':forms.TextInput(attrs={'class':'form-control'}),
        }