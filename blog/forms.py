from django import forms

from .models import clientaccount

class accountform(forms.ModelForm):

    class Meta:
        model = clientaccount
        fields = ('name', 'mobile','email', 'address','accounttype')
