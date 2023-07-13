from email.policy import default
from random import choices
from django.db import models

# Create your models here.
 

# reg_choice=(("Amhara Region Prison Police","Amhara Region Prison Police"))
court_choice = (('court one', 'court one'),('court 2','court 2'))
reasons_choice = (("በአመክሮ", "በአመክሮ"),
("በነፃ ተሰናበተ", "በነፃ ተሰናበተ"), (" በበቂ ተሰናበተ", " በበቂ ተሰናበተ"), ("ክሱ የተቋረጠ", "ክሱ የተቋረጠ"), ("በዋስ ተለቀቀ", "በዋስ ተለቀቀ"),
("በገደብ ተፈታ", "በገደብ ተፈታ"), ("የገንዘብ ቅጣት", "የገንዘብ ቅጣት"), ("ፍርዱን ጨርሶ ተፈታ", "ፍርዱን ጨርሶ ተፈታ"), 
("ዋስትና የተፈቀደለት", "ዋስትና የተፈቀደለት"), ("ሞቶ ፋይሉ ተዘጋ", "ሞቶ ፋይሉ ተዘጋ"), ("የጠፋ", "የጠፋ"), ("በይቅርታ", "በይቅርታ"),)
place_choice=(('sebatamit','sebatamit'),('kalitie','kalitie'),('d/markos','d/markos'),('shewarobit','sewarobit'),
("ziway","ziway"),)

class CentralPrison(models.Model):
    Name=models.CharField(max_length=100,default="Amhara Region Prison Police") 
    
    def __str__(self):
        return self.Name
        
class Prison(models.Model): 
    PrisonName=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    Region = models.ForeignKey(CentralPrison,null=True,   on_delete=models.CASCADE)

    # Region=models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.PrisonName

class Court(models.Model):
    CourtName = models.CharField(max_length=200, null=True, choices=court_choice, blank=True)

    def __str__(self):
        return self.CourtName

class Release(models.Model):
    Reason = models.CharField(max_length=200, null=True,choices=reasons_choice, blank=True)

    def __str__(self):
        return self.Reason

class Transfer(models.Model):
    Place = models.CharField(max_length=200, null=True,choices=place_choice, blank=True)

    def __str__(self):
     return self.Place
