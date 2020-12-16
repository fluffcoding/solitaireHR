from django.db import models
from tinymce import models as tinymce_models
from django_countries.fields import CountryField
from django.contrib.auth import get_user_model

User = get_user_model()


choices = {
    'salary_type' : [
        (0,'Daily'),
        (1,'Weekly'),
        (2,'Monthly'),
        (3,'Yearly'),
    ],
    'salary':[(x,x*5000) for x in range(50)  ],
    'gender':[
        (0,'No preference'),
        (1,'Male'),
        (2,'Female')
    ],
    'job_type':[
        (0,'Internship'),
        (1,'Freelancing'),
        (3,'Contract'),
        (4,'Full time'),
        (5,'Part time'),
        (6,'Permanent')
    ],
    'job_shift':[
        (0,'All'),
        (1,'Morning'),
        (2,'Evening'),
        (3,'Night')
    ],
    'experience' :[(x,f'{x} years') for x in range(1,36)],
    'career_level' : [
        (0, 'Intermediate'),
        (1, 'Experienced Professional'),
        (2, 'Entry Level'),
        (3, 'Department Head'),
        (4, 'GM / CEO / Country Head')
    ],
    'city': [(1, 'Karachi'), (2, 'Lahore'), (3, 'Sialkot City'), (4, 'Faisalabad'), (5, 'Rawalpindi'), (6, 'Peshawar'), (7, 'Saidu Sharif'), (8, 'Multan'), (9, 'Gujranwala'), (10, 'Islamabad'), (11, 'Quetta'), (12, 'Bahawalpur'), (13, 'Sargodha'), (14, 'New Mirpur'), (15, 'Chiniot'), (16, 'Sukkur'), (17, 'Larkana'), (18, 'Shekhupura'), (19, 'Jhang City'), (20, 'Rahimyar Khan'), (21, 'Gujrat'), (22, 'Kasur'), (23, 'Mardan'), (24, 'Mingaora'), (25, 'Dera Ghazi Khan'), (26, 'Nawabshah'), (27, 'Sahiwal'), (28, 'Mirpur Khas'), (29, 'Okara'), (30, 'Mandi Burewala'), (31, 'Jacobabad'), (32, 'Saddiqabad'), (33, 'Kohat'), (34, 'Muridke'), (35, 'Muzaffargarh'), (36, 'Khanpur'), (37, 'Gojra'), (38, 'Mandi Bahauddin'), (39, 'Abbottabad'), (40, 'Dadu'), (41, 'Khuzdar'), (42, 'Pakpattan'), (43, 'Tando Allahyar'), (44, 'Vihari'), (45, 'Jaranwala'), (46, 'Kamalia'), (47, 'Kot Addu'), (48, 'Nowshera'), (49, 'Swabi'), (50, 'Dera Ismail Khan'), (51, 'Chaman'), (52, 'Charsadda'), (53, 'Kandhkot'), (54, 'Hasilpur'), (55, 'Muzaffarabad'), (56, 'Mianwali'), (57, 'Jalalpur Jattan'), (58, 'Bhakkar'), (59, 'Zhob'), (60, 'Kharian'), (61, 'Mian Channun'), (62, 'Jamshoro'), (63, 'Pattoki'), (64, 'Harunabad'), (65, 'Toba Tek Singh'), (66, 'Shakargarh'), (67, 'Hujra Shah Muqim'), (68, 'Kabirwala'), (69, 'Mansehra'), (70, 'Lala Musa'), (71, 'Nankana Sahib'), (72, 'Bannu'), (73, 'Timargara'), (74, 'Parachinar'), (75, 'Gwadar'), (76, 'Abdul Hakim'), (77, 'Hassan Abdal'), (78, 'Tank'), (79, 'Hangu'), (80, 'Risalpur Cantonment'), (81, 'Karak'), (82, 'Kundian'), (83, 'Umarkot'), (84, 'Chitral'), (85, 'Dainyor'), (86, 'Kulachi'), (87, 'Kotli'), (88, 'Gilgit'), (89, 'Hyderabad City'), (90, 'Narowal'), (91, 'Khairpur Mir’s'), (92, 'Khanewal'), (93, 'Jhelum'), (94, 'Haripur'), (95, 'Shikarpur'), (96, 'Rawala Kot'), (97, 'Hafizabad'), (98, 'Lodhran'), (99, 'Malakand'), (100, 'Attock City'), (101, 'Batgram'), (102, 'Matiari'), (103, 'Ghotki'), (104, 'Naushahro Firoz'), (105, 'Alpurai'), (106, 'Bagh'), (107, 'Daggar'), (108, 'Bahawalnagar'), (109, 'Leiah'), (110, 'Tando Muhammad Khan'), (111, 'Chakwal'), (112, 'Khushab'), (113, 'Badin'), (114, 'Lakki'), (115, 'Rajanpur'), (116, 'Dera Allahyar'), (117, 'Shahdad Kot'), (118, 'Pishin'), (119, 'Sanghar'), (120, 'Upper Dir'), (121, 'Thatta'), (122, 'Dera Murad Jamali'), (123, 'Kohlu'), (124, 'Mastung'), (125, 'Dasu'), (126, 'Athmuqam'), (127, 'Loralai'), (128, 'Barkhan'), (129, 'Musa Khel Bazar'), (130, 'Ziarat'), (131, 'Gandava'), (132, 'Sibi'), (133, 'Dera Bugti'), (134, 'Eidgah'), (135, 'Turbat'), (136, 'Uthal'), (137, 'Khuzdar'), (138, 'Chilas'), (139, 'Kalat'), (140, 'Panjgur'), (141, 'Gakuch'), (142, 'Qila Saifullah'), (143, 'Kharan'), (144, 'Aliabad'), (145, 'Awaran'), (146, 'Dalbandin')],
    'marital_status': [(0,'Married'), (1, 'Single'), (2, 'Widowed'), (3, 'Separated')],
    'degree_level': [(0,'Non-matriculation'), (1, 'Matriculation/O-level'), (2,'Intermediate/A-level'), (3, 'Bachelors'), (4, 'Masters'), (5, 'MPhil/MS'), (6, 'PhD/Doctorate'),(7,'Certification'), (8, 'Diploma'), (9, 'Short Course')],
    'company_type': [(0, 'Sole Proprietarship'), (1, 'Public'), (2, 'Private'), (3, 'NGO')],
    'number_of_employees': [(0, '1-10'), (1, '11-50'), (2, '51-200'),(3, '201-500'),(4, '500+')],
    
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
    job_type = models.SmallIntegerField(choices=choices['job_type'], null=True)
    city = models.IntegerField(choices=choices['city'])
    job_shift = models.SmallIntegerField(choices=choices['job_shift'], null=True)
    functional_area = models.ForeignKey(FunctionalArea, on_delete=models.CASCADE)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    # career_level = models.ForeignKey(CareerLevel, on_delete=models.CASCADE)
    career_level = models.SmallIntegerField(choices=choices['career_level'], null=True)
    experience = models.SmallIntegerField(choices=choices['experience'], null=True, blank=True)
    salary_type = models.SmallIntegerField(choices=choices['salary_type'], null=True, blank=True)
    minimum_salary = models.IntegerField(choices=choices['salary'], null=True, blank=True)
    max_salary = models.IntegerField(choices=choices['salary'], null=True, blank=True)
    gender = models.SmallIntegerField(choices=choices['gender'], null=True, blank=True)
    


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


    