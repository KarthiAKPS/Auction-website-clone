from django import forms
from django.forms import ModelForm
from .models import listing, bid, comment, Category


class ListingForm(ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.values_list('category', flat=True),
        label='Category',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    class Meta:
        model = listing
        fields = ('title', 'description', 'price', 'category', 'image')
        widgets={
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control'}),
            'image' : forms.FileInput(attrs={'width':'100'})
            }
        labels={
            'title' : 'Title',
            'description': 'Description',
            'price':'Price',
            'category':'Category',
            'image':'Add Image'
            }

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