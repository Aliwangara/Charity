from django import forms
from main_app.models import Volunteers, cause, Event, happy_customers, Number


class Volunteer_form(forms.ModelForm):
    
    class Meta:
        model = Volunteers
        fields = "__all__"
        
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date" , "min": "1990-01-01", "max": "2006-01-01" }),
            "duration":forms.NumberInput(attrs={"max":20, "min":5}),
        }  
        
        
        labels = {
            "dob": "Date Of Birth",
            "email": "Email Address"
        }

class Causes_form(forms.ModelForm):
    
   class Meta:
       model = cause
       fields =['Title', 'profile', 'summary', 'info']
       
       
       
class Event_forms(forms.ModelForm):
    
    class Meta:
        model = Event
        fields = ['name', 'profile', 'About', 'subject', 'is_new', 'is_superuser']
        

class Happy_customers_form(forms.ModelForm):
    
    class Meta:
        model = happy_customers
        fields ="__all__"
        
        
class Number_form(forms.ModelForm):
    
    class Meta:
        model = Number
        fields = ['name','number']