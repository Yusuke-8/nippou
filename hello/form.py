from django import forms
from .models import Friend

class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']

class FindForm(forms.Form):
    # id = forms.IntegerField(label='ID', required=False, widget=forms.NumberInput(attrs={'class':'form-control'}))
    name = forms.CharField(label='Name', required=False, widget=forms.TextInput(attrs={'class':'form-control'}))