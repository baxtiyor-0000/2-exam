from django import forms
from .models import Questions

class Contact(forms.ModelForm):
    class Meta:
        model = Questions
        fields = ("name", "email", "question")