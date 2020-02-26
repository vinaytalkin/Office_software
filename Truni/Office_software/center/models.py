from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login, logout, authenticate


# Create your models here.
class RequestTracker(models.Model):
    client_ip = models.CharField(max_length=250, blank=True,null=True)
    request_url = models.CharField(max_length=250, blank=True,null=True)
    resp_code = models.CharField(max_length=250, blank=True,null=True)

class Registration(models.Model):
    # photoimage = models.FileField(blank=True, null=True)
    user_id = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=250, blank=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    SEX = (
        ('F', 'Female'),
        ('M', 'Male'),
        ('U', 'Unsure'),
    )
    gender = models.CharField(choices=SEX, max_length=10)
    email_id = models.EmailField(max_length=250)
    father_name = models.CharField(max_length=100)
    joining_date = models.DateField(blank=True)
    dob = models.DateField(blank=True)
    spouse_name = models.CharField(max_length=100)
    current_residency_address = models.CharField(max_length=100)
    current_zip_code = models.CharField(max_length=20)
    current_state = models.CharField(max_length=100)
    current_country = models.CharField(max_length=100)
    permanent_address = models.CharField(max_length=100)
    permanent_zip_code = models.CharField(max_length=20)
    permanent_state = models.CharField(max_length=100)
    permanent_country = models.CharField(max_length=100)
    personal_contact_no = models.IntegerField(blank=True)
    emergency_contact_no = models.IntegerField(blank=True)
    highest_education = models.CharField(max_length=250, blank=True)
    educational_institute_name = models.CharField(max_length=250, blank=True)
    year_of_passing = models.DateField(blank=True)
    previous_employee_name = models.CharField(max_length=250, blank=True)
    previous_empoyee_from = models.DateField(blank=True)
    previous_empoyee_to = models.DateField(blank=True)
    # photoidproofimage = models.FileField(blank=True, null=True)
    pan_no = models.CharField(max_length=250, blank=True)
    bank_details_for_salary = models.CharField(max_length=100)
    active_user = models.BooleanField()
    Empinfo = (
        ('F', 'Full Time'),
        ('P', 'Part Time'),
        ('O', 'Other'),
    )
    employee_info = models.CharField(choices=Empinfo, max_length=10)
    agreeterms = models.BooleanField()

    def __str__(self):
        return self.user_id


class UserImagesUpload(models.Model):
    name = models.CharField(max_length=50)
    userprofile = models.ImageField(upload_to='images/')

