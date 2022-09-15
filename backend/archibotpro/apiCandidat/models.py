from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Candidat(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    adress = models.CharField(max_length=200, blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True)
    niveau_etudes = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.last_name

class Recruteur(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    entreprise = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    telephone = models.CharField(max_length=200, blank=True)
    needed_profile = models.CharField(max_length=200, blank=True)
    crenaux_proposé = models.DateTimeField(null=True,blank=True)
    appel_telephonique = models.BooleanField(default=False)
    piece_jointe = models.FileField(upload_to='documents/', blank=True)
    def __str__(self):
        return self.last_name

class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    service = models.CharField(max_length=30)
    telephone = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254)
    appel_telephonique = models.BooleanField(default=False)
    piece_jointe = models.FileField(upload_to='documents/', blank=True)
    def __str__(self):
        return self.last_name

class Partenaire(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    type_partenariat = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=200, blank=True)
    email = models.EmailField(max_length=254)
    appel_telephonique = models.BooleanField(default=False)
    date_crenaux = models.DateTimeField(null=True,blank=True)
    piece_jointe = models.FileField(upload_to='documents/', blank=True)
    def __str__(self):
        return self.last_name



class Offre(models.Model):
    titre = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    type_contrat = models.CharField(max_length=100)
    salaire  = models.IntegerField(null=True,blank=True)
    entreprise = models.CharField(max_length=100)
    mode = models.CharField(max_length=100) #presentiel à distance
    location = models.CharField(max_length=200)


class Meeting(models.Model):
    date = models.DateField() #no weekends
    time_start = models.TimeField() # from 8:00 AM to 5:00 PM
    time_end = models.TimeField() 
    title = models.CharField(max_length=200,null=True,blank=True)
    details = models.TextField(null=True,blank=True)