from django.db import models
from tinymce import models as tinymce_models
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model

User = get_user_model()


choices = {
    'salary_type' : [
        ('Daily','Daily'),
        ('Weekly','Weekly'),
        ('Monthly','Monthly'),
        ('Yearly','Yearly'),
    ],
    'salary':[(x*5000,x*5000) for x in range(50)],
    'gender':[
        ('No preference','No preference'),
        ('Male','Male'),
        ('Female','Female')
    ],
    'job_type':[
        ('Internship','Internship'),
        ('Freelancing','Freelancing'),
        ('Contract','Contract'),
        ('Full time','Full time'),
        ('Part time','Part time'),
        ('Permanent','Permanent')
    ],
    'job_shift':[
        ('All','All'),
        ('Morning','Morning'),
        ('Evening','Evening'),
        ('Night','Night')
    ],
    'experience' :[(f'{x} years',f'{x} years') for x in range(1,36)],
    'career_level' : [
        ('Intermediate', 'Intermediate'),
        ('Experienced Professional', 'Experienced Professional'),
        ('Entry Level', 'Entry Level'),
        ('Department Head', 'Department Head'),
        ('GM / CEO / Country Head', 'GM / CEO / Country Head')
    ],
    'city': [('Karachi', 'Karachi'), ('Lahore', 'Lahore'), ('Sialkot City', 'Sialkot City'), ('Faisalabad', 'Faisalabad'), ('Rawalpindi', 'Rawalpindi'), ('Peshawar', 'Peshawar'), ('Saidu Sharif', 'Saidu Sharif'), ('Multan', 'Multan'), ('Gujranwala', 'Gujranwala'), ('Islamabad', 'Islamabad'), ('Quetta', 'Quetta'), ('Bahawalpur', 'Bahawalpur'), ('Sargodha', 'Sargodha'), ('New Mirpur', 'New Mirpur'), ('Chiniot', 'Chiniot'), ('Sukkur', 'Sukkur'), ('Larkana', 'Larkana'), ('Shekhupura', 'Shekhupura'), ('Jhang City', 'Jhang City'), ('Rahimyar Khan', 'Rahimyar Khan'), ('Gujrat', 'Gujrat'), ('Kasur', 'Kasur'), ('Mardan', 'Mardan'), ('Mingaora', 'Mingaora'), ('Dera Ghazi Khan', 'Dera Ghazi Khan'), ('Nawabshah', 'Nawabshah'), ('Sahiwal', 'Sahiwal'), ('Mirpur Khas', 'Mirpur Khas'), ('Okara', 'Okara'), ('Mandi Burewala', 'Mandi Burewala'), ('Jacobabad', 'Jacobabad'), ('Saddiqabad', 'Saddiqabad'), ('Kohat', 'Kohat'), ('Muridke', 'Muridke'), ('Muzaffargarh', 'Muzaffargarh'), ('Khanpur', 'Khanpur'), ('Gojra', 'Gojra'), ('Mandi Bahauddin', 'Mandi Bahauddin'), ('Abbottabad', 'Abbottabad'), ('Dadu', 'Dadu'), ('Khuzdar', 'Khuzdar'), ('Pakpattan', 'Pakpattan'), ('Tando Allahyar', 'Tando Allahyar'), ('Vihari', 'Vihari'), ('Jaranwala', 'Jaranwala'), ('Kamalia', 'Kamalia'), ('Kot Addu', 'Kot Addu'), ('Nowshera', 'Nowshera'), ('Swabi', 'Swabi'), ('Dera Ismail Khan', 'Dera Ismail Khan'), ('Chaman', 'Chaman'), ('Charsadda', 'Charsadda'), ('Kandhkot', 'Kandhkot'), ('Hasilpur', 'Hasilpur'), ('Muzaffarabad', 'Muzaffarabad'), ('Mianwali', 'Mianwali'), ('Jalalpur Jattan', 'Jalalpur Jattan'), ('Bhakkar', 'Bhakkar'), ('Zhob', 'Zhob'), ('Kharian', 'Kharian'), ('Mian Channun', 'Mian Channun'), ('Jamshoro', 'Jamshoro'), ('Pattoki', 'Pattoki'), ('Harunabad', 'Harunabad'), ('Toba Tek Singh', 'Toba Tek Singh'), ('Shakargarh', 'Shakargarh'), ('Hujra Shah Muqim', 'Hujra Shah Muqim'), ('Kabirwala', 'Kabirwala'), ('Mansehra', 'Mansehra'), ('Lala Musa', 'Lala Musa'), ('Nankana Sahib', 'Nankana Sahib'), ('Bannu', 'Bannu'), ('Timargara', 'Timargara'), ('Parachinar', 'Parachinar'), ('Gwadar', 'Gwadar'), ('Abdul Hakim', 'Abdul Hakim'), ('Hassan Abdal', 'Hassan Abdal'), ('Tank', 'Tank'), ('Hangu', 'Hangu'), ('Risalpur Cantonment', 'Risalpur Cantonment'), ('Karak', 'Karak'), ('Kundian', 'Kundian'), ('Umarkot', 'Umarkot'), ('Chitral', 'Chitral'), ('Dainyor', 'Dainyor'), ('Kulachi', 'Kulachi'), ('Kotli', 'Kotli'), ('Gilgit', 'Gilgit'), ('Hyderabad City', 'Hyderabad City'), ('Narowal', 'Narowal'), ('Khairpur Mir’s', 'Khairpur Mir’s'), ('Khanewal', 'Khanewal'), ('Jhelum', 'Jhelum'), ('Haripur', 'Haripur'), ('Shikarpur', 'Shikarpur'), ('Rawala Kot', 'Rawala Kot'), ('Hafizabad', 'Hafizabad'), ('Lodhran', 'Lodhran'), ('Malakand', 'Malakand'), ('Attock City', 'Attock City'), ('Batgram', 'Batgram'), ('Matiari', 'Matiari'), ('Ghotki', 'Ghotki'), ('Naushahro Firoz', 'Naushahro Firoz'), ('Alpurai', 'Alpurai'), ('Bagh', 'Bagh'), ('Daggar', 'Daggar'), ('Bahawalnagar', 'Bahawalnagar'), ('Leiah', 'Leiah'), ('Tando Muhammad Khan', 'Tando Muhammad Khan'), ('Chakwal', 'Chakwal'), ('Khushab', 'Khushab'), ('Badin', 'Badin'), ('Lakki', 'Lakki'), ('Rajanpur', 'Rajanpur'), ('Dera Allahyar', 'Dera Allahyar'), ('Shahdad Kot', 'Shahdad Kot'), ('Pishin', 'Pishin'), ('Sanghar', 'Sanghar'), ('Upper Dir', 'Upper Dir'), ('Thatta', 'Thatta'), ('Dera Murad Jamali', 'Dera Murad Jamali'), ('Kohlu', 'Kohlu'), ('Mastung', 'Mastung'), ('Dasu', 'Dasu'), ('Athmuqam', 'Athmuqam'), ('Loralai', 'Loralai'), ('Barkhan', 'Barkhan'), ('Musa Khel Bazar', 'Musa Khel Bazar'), ('Ziarat', 'Ziarat'), ('Gandava', 'Gandava'), ('Sibi', 'Sibi'), ('Dera Bugti', 'Dera Bugti'), ('Eidgah', 'Eidgah'), ('Turbat', 'Turbat'), ('Uthal', 'Uthal'), ('Khuzdar', 'Khuzdar'), ('Chilas', 'Chilas'), ('Kalat', 'Kalat'), ('Panjgur', 'Panjgur'), ('Gakuch', 'Gakuch'), ('Qila Saifullah', 'Qila Saifullah'), ('Kharan', 'Kharan'), ('Aliabad', 'Aliabad'), ('Awaran', 'Awaran'), ('Dalbandin', 'Dalbandin')],
    'marital_status': [('Married','Married'), ('Single', 'Single'), ('Widowed', 'Widowed'), ('Separated', 'Separated')],
    'degree_level': [('Non-matriculation','Non-matriculation'), ('Matriculation/O-level', 'Matriculation/O-level'), ('Intermediate/A-level','Intermediate/A-level'), ('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('MPhil/MS', 'MPhil/MS'), ('PhD/Doctorate', 'PhD/Doctorate'),('Certification','Certification'), ('Diploma', 'Diploma'), ('Short Course', 'Short Course')],
    'company_type': [('Sole Proprietarship', 'Sole Proprietarship'), ('Public', 'Public'), ('Private', 'Private'), ('NGO', 'NGO')],
    'number_of_employees': [( '1-10', '1-10'), ( '11-50', '11-50'), ( '51-200', '51-200'),('201-500', '201-500'),('500+', '500+')],
    'reference_type': [('Personal', 'Personal'), ('Professional', 'Professional')]
}


class Industry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = 'industries'

# class CareerLevel(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


class FunctionalArea(models.Model):
    name = models.CharField(max_length=100)


    def __str__(self):
        return self.name


class Job(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    job_designation = models.CharField(max_length=100)
    # job_description = tinymce_models.HTMLField()
    job_description = models.TextField()
    country = CountryField(default='PK')
    job_type = models.CharField(max_length=50, choices=choices['job_type'], null=True)
    city = models.CharField(max_length=50, choices=choices['city'])
    job_shift = models.CharField(max_length=50, choices=choices['job_shift'], null=True)
    functional_area = models.ForeignKey(FunctionalArea, on_delete=models.CASCADE, null=True, blank=True)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    # career_level = models.ForeignKey(CareerLevel, on_delete=models.CASCADE)
    career_level = models.CharField(max_length=50, choices=choices['career_level'], null=True)
    experience = models.CharField(max_length=50, choices=choices['experience'], null=True, blank=True)
    salary_type = models.CharField(max_length=50, choices=choices['salary_type'], null=True, blank=True)
    minimum_salary = models.IntegerField(choices=choices['salary'], null=True, blank=True)
    max_salary = models.IntegerField(choices=choices['salary'], null=True, blank=True)
    gender = models.CharField(max_length=50, choices=choices['gender'], null=True, blank=True)
    


class JobApplication(models.Model):
    job_seeker = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    expected_salary_minimum = models.IntegerField(choices=choices['salary'])
    expected_salary_maximum = models.IntegerField(choices=choices['salary'])
    applied = models.BooleanField(default=True, null=True, blank=True)
    shortlisted = models.BooleanField(null=True, blank=True)
    interviewed = models.BooleanField(null=True, blank=True)
    selected = models.BooleanField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)


    def is_rejected(self):
        if self.applied == False or self.shortlisted == False or self.interviewed == False or self.selected == False:
            return True
        else:
            return False
    
    def is_accepted(self):
        if self.applied == True and self.shortlisted == True and self.interviewed == True and self.selected == True:
            return True
        else:
            return False