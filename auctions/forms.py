from django import forms
from django.http import request
from django.forms import ModelForm
from .models import listing, bid, comment, Category, User


class ListingForm(ModelForm):
    
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget = forms.Select(attrs={'class':'form-select'}))

    class Meta:
        model = listing
        fields = ('title', 'description', 'price', 'category', 'image', 'posted_user')
        widgets={
            'title' : forms.TextInput(attrs={'class':'form-select'}),
            'description' : forms.TextInput(attrs={'class':'form-select'}),
            'price' : forms.NumberInput(attrs={'class':'form-select'}),
            'image' : forms.FileInput(attrs={'class':'form-select-file'}),
            'posted_user' : forms.HiddenInput()
            }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['posted_user'].required = False


class BidsForm(ModelForm):
    class Meta:
        model = bid
        fields = ("cur",)
        widgets={
            'cur' : forms.NumberInput(attrs={'class':'form-control', "width":'50'}),
            }
        labels={
            'cur':'Place your Bid',
            }