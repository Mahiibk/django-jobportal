from django.db import models

# Create your models here.
class Hydjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    eligiblity = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()


class Bengjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    eligiblity = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()

class Deljobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    eligiblity = models.CharField(max_length=30)
    address = models.CharField(max_length=80)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()