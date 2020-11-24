from django import forms
from .models import Student,Internship,InternshipAssignment
from django.forms import ModelChoiceField

class StudentSearchForm(forms.Form):



   first_name = forms.ModelChoiceField(queryset=Student.objects.values_list("first_name", flat=True).distinct(),empty_label=None)
   last_name = forms.ModelChoiceField(queryset=Student.objects.values_list("last_name", flat=True).distinct(),empty_label=None)
   #first_name= forms.ModelChoiceField(queryset=Student.objects.values_list("last_name"), flat=empty_label="----", to_field_name="first_name")
   #last_name= forms.ModelChoiceField(queryset=Student.objects.all(), empty_label="----", to_field_name="last_name")

   class Meta:
     model = Student
     fields = [
             "first_name",
             "last_name"
        ]
     # first_name = forms.ModelChoiceField(queryset = Student.objects.all())



class InternshipSearchForm(forms.ModelForm):
   class Meta:
     model = Internship
     fields = ['organization_name', 'supervisor_name']


class InternshipAssignmentSearchForm(forms.ModelForm):
   class Meta:
     model = InternshipAssignment
     fields = ['semester', 'year']
