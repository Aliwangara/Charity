from django import forms
from .models import Employee


class Employee_form(forms.ModelForm):
    
    class Meta:
        model = Employee
        fields = '__all__'
        
        widgets = {
            "dob": forms.DateInput(attrs={"type": "date" , "min": "1990-01-01", "max": "2006-01-01" }),
            "duration":forms.CharField(attrs={"max":20, "min":5}),
        }  
        
        
        labels = {
            "dob": "Date Of Birth",
            "email": "Email Address"
        }