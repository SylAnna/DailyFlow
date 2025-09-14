from django import forms
from .models import List, Category


class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["item", "completed", "category","date"]
