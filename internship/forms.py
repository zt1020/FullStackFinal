from django import forms
from .models import Student,Internship


class StudentSearchForm(forms.ModelForm):
   class Meta:
     model = Student
     fields = ['first_name', 'last_name']


class InternshipSearchForm(forms.ModelForm):
   class Meta:
     model = Internship
     fields = ['organization_name', 'supervisor_name']
