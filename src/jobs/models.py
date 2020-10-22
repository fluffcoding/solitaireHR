from django.db import models
from tinymce import models as tinymce_models
from django_countries.fields import CountryField
import calendar
choices = {
    'salary_type' : [
        (0,'Daily'),
        (1,'Weekly'),
        (2,'Monthly'),
        (3,'Yearly'),
    ],
    'salary':[(x,x*5000) for x in range(50)  ],
    'gender':[
        (0,'no preference'),
        (1,'male'),
        (2,'female')
    ],
    'job_type':[
        (0,'internship'),
        (1,'freelancing'),
        (3,'contract'),
        (4,'full time'),
        (5,'part time'),
        (6,'permanent')
    ],
    'job_shift':[
        (0,'all'),
        (1,'morning'),
        (2,'evening'),
        (3,'night')
    ],
    'experience' :[(x,f'{x} years') for x in range(1,36)]
    
}


class Industry(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class CareerLevel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Job(models.Model):
    job_designation = models.CharField(max_length=100)
    job_description = tinymce_models.HTMLField()
    country = CountryField()
    job_type = models.SmallIntegerField()
    city = models.CharField(max_length=100)
    job_shift = models.SmallIntegerField()
    functional_area = models.SmallIntegerField()
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    career_level = models.ForeignKey(CareerLevel, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=choices['experience'])
    salary_type = models.SmallIntegerField(choices=choices['salary_type'])
    minimum_salary = models.IntegerField(choices=choices['salary'])
    max_salary = models.IntegerField(choices=choices['salary'])
    gender = models.SmallIntegerField(choices=choices['gender'])
    

    