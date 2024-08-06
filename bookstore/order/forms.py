from django import forms
from .models import Order

# city Choices is names of Cities in Canada

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Calgary', 'Calgary'),
		('Edmonton', 'Edmonton'),
		('Lethbridge', 'Lethbridge'),
		('Red Deer', 'Red Deer'),
		('Regina', 'Regina'),

		('Toronto', 'Toronto'),
		('Vancouver', 'Vancouver'),
		('Winnipeg', 'Winnipeg'),
		('Kitchener', 'Kitchener'),

		('Montreal', 'Montreal'),
		('Quebec', 'Quebec'),
		('Sherbrooke', 'Sherbrooke'),
		('Laval', 'Laval'),
		('Gatineau', 'Gatineau'),

	)

	DISCRICT_CHOICES = (
		('Alberta', 'Alberta'),
		('British Columbia', 'British Columbia'),
		('Manitoba', 'Manitoba'),
		('New Brunswick', 'New Brunswick'),
		('Newfoundland and Labrador', 'Newfoundland and Labrador'),
		('Nova Scotia', 'Nova Scotia'),
		('Ontario', 'Ontario'),
	)

	PAYMENT_METHOD_CHOICES = (
		('Paypal', 'Paypal'),
		('Credit Card','Credit Card')
	)

	city = forms.ChoiceField(choices=DIVISION_CHOICES)
	province =  forms.ChoiceField(choices=DISCRICT_CHOICES)
	payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'city', 'province', 'postal_code', 'payment_method', 'account_no', 'transaction_id']
