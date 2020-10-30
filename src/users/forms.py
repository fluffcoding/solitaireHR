from allauth.account.forms import SignupForm
from django import forms


class myForm(SignupForm):

	def signup(self, user):
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.save()
		return user
