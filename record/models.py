from platform import release
from sre_constants import MAX_UNTIL
from tkinter import CASCADE, Image
from turtle import width
from winreg import SaveKey
from django.db import models
from account.models import User 
from django.forms import DateTimeField
from django.contrib.auth.models import AbstractUser
from prison.models import *
from multiselectfield import MultiSelectField
from datetime import date
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

    
# class Crime(models.Model): 
#     CrimeName=models.CharField(max_length=100)
#     Discription=models.CharField(max_length=200) 
#     createdby = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
#     def __str__(self):
#         return self.CrimeName

cat_choice=(
    ("Criteria1","Criteria1"),
    ("Criteria2","Criteria2")
)
item_choice=(
    ("Money","Money"),
    ("Food","Food"),("Cloth","Cloth")
)
GENDER=(('Female','Female'),('Male','Male'))
BLOODTYPES=(('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'), ('O+','O+'),('O-','O-'))
ALLOWED=(('Yes','Yes'),('No','No'))

class Criminal(models.Model):
     
    CriminalName=models.CharField(max_length=200, null=True)
    CourtName=models.ForeignKey(Court, on_delete=models.CASCADE, null=True)
    Age=models.PositiveIntegerField( null=True)
    Height=models.FloatField(validators=[MinValueValidator(1), MaxValueValidator(2.5)],null=True)
    EyeColor=models.CharField(max_length=100,null=True) 
    Gender=models.CharField(max_length=8,null=True , choices=GENDER)  
    Personality=models.CharField(max_length=100, null=True)
    Nationality=models.CharField(max_length=100,null=True)
    EntranceDate=models.DateField(auto_now=True,null=True)
    EntranceTime=models.TimeField(null=True)
    ReleasedDate=models.DateField(null=True)
    TimeLeft=models.CharField(max_length=100,null=True, blank=True)
    Guardian=models.CharField(max_length=100,null=True)
    Bloodtype=models.CharField(max_length=30,null=True, choices=BLOODTYPES)
    AssignedCellNumber=models.PositiveIntegerField(null=True)
    Status= models.BooleanField(default=True)
    ImprisonmentTime=models.PositiveIntegerField(null=True) 
    Address=models.CharField(max_length=100,null=True) 
    Category=MultiSelectField(max_length=20,choices=cat_choice, null=True)
    CrimeDescription=models.TextField(max_length=200, null=True, blank=True)
    VisitorsAllowed=models.CharField(max_length=50, null=True, choices=ALLOWED)
    prison=models.ForeignKey(Prison,on_delete=models.CASCADE ,null=True)
    createdby = models.ForeignKey(User,null=True ,on_delete=models.CASCADE)
    Transfer=models.ForeignKey(Transfer, null=True, on_delete=models.CASCADE)
    Reason_For_Release = models.ForeignKey(Release,  null=True, on_delete=models.CASCADE)
    
    

    # def tl(self, *args, **kwargs):
    #     self.TimeLeft=(self.ReleasedDate - self.EntranceDate)
    #     super().save(*args, **kwargs)
    
    #     return self.TimeLeft

    def __str__(self):
        return self.CriminalName

    @property
    def Days_till(self):
        days_till= self.ReleasedDate - self.EntranceDate  
        days_till_stripped= str(days_till).split(',')[0]
        return days_till_stripped

    # @property
    # def Is_Past(self):
    #     today=date.today()
    #     if self.ReleasedDate < today:
    #         result= "Past"
    #     else:
    #         result= "Future"
    #     return result
    

class Visitor(models.Model): 
    Name=models.CharField(max_length=200,null=True)
    Gender=models.CharField(max_length=8 ,null=True )
    Address=models.CharField(max_length=200,null=True)
    Nationality=models.CharField(max_length=200,null=True)
    VisitDate=models.DateField(auto_now=True)
    VisitedCriminal=models.ForeignKey(Criminal, null=True, on_delete= models.SET_NULL)
    Item=models.CharField(max_length=20, null=True, choices=item_choice, blank=True)   
    createdby = models.ForeignKey(User,null=True, on_delete=models.CASCADE)
    prison=models.ForeignKey(Prison,on_delete=models.CASCADE ,null=True)
    
    
    def __str__(self):
        return self.Name



