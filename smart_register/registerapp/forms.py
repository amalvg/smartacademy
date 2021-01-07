from . models import register
from django import forms
class Registerforms(forms.ModelForm):
    class Meta:
        model=register
        fields=['name','address','dob','mob','qual','email','pname','pmob','course','img']