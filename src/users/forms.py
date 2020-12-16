from allauth.account.forms import SignupForm
from django import forms
from .models import Profile

from bootstrap_datepicker_plus import DatePickerInput

class myForm(SignupForm):

	def signup(self, user):
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.save()
		return user


class DateInput(forms.DateInput):
    input_type = 'date'


class profileForm1(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('full_name',
'date_of_birth',
'gender',
'website',
'mobile_phone',)
		widgets = {
            'date_of_birth': DateInput(),
        }



class profileForm2(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('country',
'city',
'address_line1',
'address_line2',
'zip_code')



class profileForm3(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('preferred_job_designation',
'preferred_job_city',
'expected_salary',
)


class profileForm4(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('current_designation',
'current_company','experience')



class profileForm5(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('company',
'company_type',
'company_country',
'city',
'branch_name',
'website',
'phone',
'address',
'number_of_employees',
'industry',
'operating_since',)