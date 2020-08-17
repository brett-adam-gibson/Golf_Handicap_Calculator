from django import forms
from .models import *

class PostRound(forms.ModelForm):
    class Meta:
        model = 