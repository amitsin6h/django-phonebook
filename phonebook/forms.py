from django import forms
from . models import PhoneBook


class PhoneBookForm(forms.ModelForm):
	class Meta:
		model = PhoneBook
		fields = ('name', 'phone', 'email', 'address')
	
	def __init__(self, *args, **kwargs):
		super(PhoneBookForm, self).__init__(*args, **kwargs)
		self.fields['name'].widget = forms.TextInput(attrs={'placeholder':'Name'})
		self.fields['phone'].widget = forms.TextInput(attrs={'placeholder':'Phone'})
		self.fields['email'].widget = forms.TextInput(attrs={'placeholder':'Email'})
		self.fields['address'].widget = forms.TextInput(attrs={'placeholder':'Address'})