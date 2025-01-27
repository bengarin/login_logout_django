from django import forms
from .models import Category,Subcategory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'})
        }
class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['name',"category"]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter category name'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

class CustomizeFormUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
                