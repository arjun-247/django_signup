from app3.models import *
from django import forms

class dataform(forms.ModelForm):
    class Meta:
        model=database1
        fields='__all__'