from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, Inventory_item

class User_register_form(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

#fixed: type error
class Inventory_item_form(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=Category.objects.all())
	
	class Meta:
		model = Inventory_item
		fields = ['name', 'quantity', 'category']