
from django import forms
from .models import Compliment

class complimentForm(forms.Form):
    
    class Meta:
        model = Compliment
        fields = ['number','sender','compliment']