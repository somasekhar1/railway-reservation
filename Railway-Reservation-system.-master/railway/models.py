from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class registrationpage(models.Model):
    firstname=models.CharField(max_length=10)
    lastname=models.CharField(max_length=10)
    surname=models.CharField(max_length=10)
    fathername=models.CharField(max_length=10)
    cno=models.IntegerField(default=10,primary_key=True)
    email=models.EmailField()
    username=models.CharField(max_length=10)
    password=models.CharField(max_length=10)
    address=models.CharField(max_length=10)


class ticketbooking(models.Model):
    fromplace=models.CharField(max_length=10)
    toplace=models.CharField(max_length=10)
    date=models.DateField()
    journeydate=models.DateField()
    searchtrain=models.CharField(max_length=10)

class payment(models.Model):
    cardtype=models.CharField(max_length=5)
    bankname=models.CharField(max_length=15)
    cardholdername=models.CharField(max_length=10)
    cardnumber=models.IntegerField(default=11)
    cvvno=models.IntegerField(default=3)

