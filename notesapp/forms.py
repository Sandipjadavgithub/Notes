from django import forms
from .models import*

class Noteform(forms.ModelForm):
    class Meta:
        model = Note
        fields ="__all__"

