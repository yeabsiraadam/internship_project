from dataclasses import fields
from tkinter import Widget
from django import forms
from soupsieve import select
from .models import *
from prison.models import * 
from multiselectfield import MultiSelectField
#from datetimepicker.widgets import DateTimePicker
from django.forms.widgets import NumberInput
  

GENDER=(('Female','Female'),('Male','Male'))
BLOODTYPES=(('A+','A+'),('A-','A-'),('B+','B+'),('B-','B-'),('AB+','AB+'),('AB-','AB-'), ('O+','O+'),('O-','O-'))
REG=(("Amhara Region Prison Police","Amhara Region Prison Police"))
ITEMS=(('________','________'),('Money','Money'),('Food','Food'),('Cloth','Cloth'))
ALLOWED=(('Yes','Yes'),('No','No'))
cat_choice=(
    ('Criteria1','Criteria1'),
    ('Criteria2','Criteria2')
)
COURT= (('--------','--------'),('court one', 'court one'), ('court 2', 'court 2'))
REASONS = (('------','--------'),("በአመክሮ", "በአመክሮ"),
("በነፃ ተሰናበተ", "በነፃ ተሰናበተ"), (" በበቂ ተሰናበተ",
                            " በበቂ ተሰናበተ"), ("ክሱ የተቋረጠ", "ክሱ የተቋረጠ"), ("በዋስ ተለቀቀ", "በዋስ ተለቀቀ"),
("በገደብ ተፈታ", "በገደብ ተፈታ"), ("የገንዘብ ቅጣት",
                            "የገንዘብ ቅጣት"), ("ፍርዱን ጨርሶ ተፈታ", "ፍርዱን ጨርሶ ተፈታ"),
("ዋስትና የተፈቀደለት", "ዋስትና የተፈቀደለት"), ("ሞቶ ፋይሉ ተዘጋ", "ሞቶ ፋይሉ ተዘጋ"), ("የጠፋ", "የጠፋ"), ("በይቅርታ", "በይቅርታ"),)
PLACE = (('------', '--------'), ('sebatamit', 'sebatamit'), ('kalitie', 'kalitie'), ('d/markos', 'd/markos'), ('shewarobit', 'sewarobit'),
                ("ziway", "ziway"),)

class DateInput(forms.DateInput):
    input_type = 'date'

class PrisonForm(forms.ModelForm):
    class Meta:
        model = Prison
        fields = '__all__'
       
# class CrimeForm(forms.ModelForm):
#     class Meta:
#         model = Crime
#         fields = '__all__'
#         exclude = ('createdby',)
         
class CriminalForm(forms.ModelForm): 
    ReleasedDate=forms.DateTimeField(widget=NumberInput(attrs={'type': 'date'}))
    Gender=forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER) 
    Category=MultiSelectField(max_length=20,choices=cat_choice,null=True)
    Bloodtype= forms.ChoiceField(choices=BLOODTYPES) 
    CourtName=forms.ChoiceField(choices=COURT)
    Transfer = forms.ChoiceField(choices=PLACE)
    Reason_For_Release = forms.ChoiceField(choices=REASONS)
    VisitorsAllowed=forms.ChoiceField(widget=forms.RadioSelect,choices=ALLOWED)
    
    class Meta:
        model=Criminal
        fields='__all__'
        exclude = ('createdby','prison','EntranceDate','TimeLeft','Status',)

class SearchForm(forms.ModelForm):
    class Meta:
        model=Criminal
        fields=['TimeLeft',]
        
class VisitorForm(forms.ModelForm):
    Gender=forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER) 
    Item= forms.ChoiceField(choices=ITEMS) 
    # VisitedCriminal=models.ForeignKey(Criminal, null=True, on_delete= models.SET_NULL)
    class Meta:
            model=Visitor 
            fields='__all__'
            exclude = ('createdby','VisitDate','prison',)


        


    
   