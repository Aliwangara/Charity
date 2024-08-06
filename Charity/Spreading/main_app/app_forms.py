from django import forms
from main_app.models import Volunteers, cause


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
       