from django import forms
from .models import Student,Internship,InternshipAssignment


class StudentSearchForm(forms.ModelForm):
   class Meta:
     model = Student
     fields = ['first_name', 'last_name']


class InternshipSearchForm(forms.ModelForm):
   class Meta:
     model = Internship
     fields = ['organization_name', 'supervisor_name']


class InternshipAssignmentSearchForm(forms.ModelForm):
   class Meta:
     model = InternshipAssignment
     fields = ['semester', 'year']
