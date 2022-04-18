from django import forms

from .models import UrlDatabase


class UpdateForm(forms.ModelForm):
    class Meta:
        model = UrlDatabase
        fields = ['user', 'link', 'status']
        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control'}),
            'link': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.TextInput(attrs={'class': 'form-control'})

        }
