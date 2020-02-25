from django.db import models

# Create your models here.
class basicmod(models.Model):

    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=250)
    body = models.TextField()
    category = models.CharField(max_length=250)


class ContactForms (models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(unique=True)
    subject = models.CharField(max_length=250)
    body = models.TextField()
    category = models.CharField(max_length=250)
    def __str__(self):
        return self.name
