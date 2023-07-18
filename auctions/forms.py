from django import forms
from django.http import request
from django.forms import ModelForm
from .models import listing, bid, comment, Category, User


class ListingForm(ModelForm):
    
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget = forms.Select(attrs={'class':'form-control'}))

    class Meta:
        model = listing
        fields = ('title', 'description', 'price', 'category', 'image', 'posted_user')
        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'image' : forms.FileInput(attrs={'class':'form-control-file'}),
            'posted_user' : forms.HiddenInput()
            }
        labels={
            'title' : 'Title',
            'description': 'Description',
            'price':'Price',
            'category':'Category',
            'image':'Add Image'
            }

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['posted_user'].required = False


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

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