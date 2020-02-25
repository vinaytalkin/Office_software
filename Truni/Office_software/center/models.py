from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import login,logout,authenticate
# Create your models here.

class Registration(models.Model):
	#photoimage = models.FileField(blank=True, null=True)
	username = models.CharField(max_length=100,unique=True)
	password = models.CharField(max_length=250,blank=False)
	firstname = models.CharField(max_length=100,unique=True)
	lastname = models.CharField(max_length=100,unique=True)
	SEX = (
		('F','Female'),
		('M','Male'),
		('U','Unsure'),
	)
	sex = models.CharField(choices=SEX,max_length=10)
	email = models.EmailField(max_length=250)
	fathername = models.CharField(max_length=100,unique=True)
	joiningdate = models.DateField()
	dob = models.DateField(blank=True)
	spousename = models.CharField(max_length=100,unique=True)
	currentresidencyaddress = models.CharField(max_length=100)
	czip_code = models.CharField(max_length=20)
	cstate = models.CharField(max_length=100)
	ccountry = models.CharField(max_length=100)
	permanentaddress = models.CharField(max_length=100)
	pzip_code = models.CharField(max_length=20)
	pstate = models.CharField(max_length=100)
	pcountry = models.CharField(max_length=100)
	personalcontactno = models.IntegerField(blank=True)
	emergencycontactno = models.IntegerField(blank=True)
	highesteducation = models.CharField(max_length=250,blank=True)
	educationalinstitutename =  models.CharField(max_length=250,blank=True)
	yearofpassing = models.DateField(blank=True)
	previousemployeename =  models.CharField(max_length=250,blank=True)
	previousempoyeefrom = models.DateField(blank=True)
	previousempoyeeto = models.DateField(blank=True)
	#photoidproofimage = models.FileField(blank=True, null=True)
	panno = models.CharField(max_length=250,blank=True)
	bankedtailsforsalary = models.CharField(max_length=100)
	activeuser = models.BooleanField()
	Empinfo = (
		('F', 'Full Time'),
		('P', 'Part Time'),
		('O', 'Other'),
	)
	employeeinfo = models.CharField(choices=Empinfo, max_length=10)


class UserImagesUpload(models.Model):
	name = models.CharField(max_length=50)
	userprofile = models.ImageField(upload_to='images/')


