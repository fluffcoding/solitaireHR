from allauth.account.forms import SignupForm
from django import forms
from .models import Profile, JobSeekerProfile, Projects, Reference

# from bootstrap_datepicker_plus import DatePickerInput

class myForm(SignupForm):

	def signup(self, user):
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.save()
		return user


class ReferenceForm(forms.ModelForm):
	class Meta:
		model = Reference
		exclude = ('job_seeker',)


class ProjectsForm(forms.ModelForm):
	class Meta:
		model = Projects
		exclude = ('job_seeker',)
		widgets = {
          'description': forms.Textarea(attrs={'rows':4}),
        }


class jobSeekerForm(forms.ModelForm):
	class Meta:
		model = JobSeekerProfile
		exclude = ('profile',)
		widgets = {
          'summary': forms.Textarea(attrs={'rows':4}),
        }

class DateInput(forms.DateInput):
    input_type = 'date'


class profileForm1(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# self.fields['date_of_birth'].required = True
		self.fields['full_name'].required = True
		self.fields['gender'].required = True
		self.fields['mobile_phone'].required = True

	class Meta:
		model = Profile
		fields = ('full_name',
'date_of_birth',
'gender',
'linked_in',
'mobile_phone',)
		widgets = {
            'date_of_birth': DateInput(),
        }



class profileForm2(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['country'].required = True
		self.fields['city'].required = True
		# self.fields['address_line1'].required = True

	class Meta:
		model = Profile
		fields = ('country',
'city',
'address_line1',
'address_line2',
'zip_code')



class profileForm3(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# self.fields['preferred_job_city'].required = True
		# self.fields['expected_salary'].required = True


	class Meta:
		model = Profile
		fields = ('preferred_job_designation',
'preferred_job_city',
'expected_salary',
)


class profileForm4(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['current_designation'].required = True
		self.fields['current_company'].required = True
	class Meta:
		model = Profile
		fields = ('current_designation',
'current_company','experience', 'current_salary')



class profileForm5(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['company'].required = True
		self.fields['company_type'].required = True
		self.fields['company_country'].required = True
		self.fields['city'].required = True
		# self.fields['number_of_employees'].required = True

	class Meta:
		model = Profile
		fields = ('company',
'company_type',
'company_country',
'city',
'branch_name',
# 'linked_in',
'website',
'phone',
'address',
'number_of_employees',
'industry',
'operating_since',)



class profileForm6(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['contact_person'].required = True
		self.fields['contact_person_phone'].required = True
		self.fields['contact_person_official_email'].required = True
	class Meta:
		model = Profile
		fields = ('contact_person','contact_person_phone','contact_person_official_email')