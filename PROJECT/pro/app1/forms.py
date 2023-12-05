from app1.models import *
from django import forms

class studentform(forms.ModelForm):
    class Meta:
        model=student
        fields='__all__'

class employeeform(forms.ModelForm):
    class Meta:
        model=employee
        fields='__all__'