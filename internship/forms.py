"""
forms.py
Contributors: Snehitha, harshani
"""
from django import forms
# from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Student, Internship, InternshipAssignment



class StudentForm(forms.ModelForm):
	"""
	Student form
	"""
	class Meta: # pylint: disable=R0903
		"""
		fields for student form
		"""
		model = Student
		fields = ['student_id','unh_id','last_name','first_name',
			'school_email','major','degree','linkedin']


class InternshipForm(forms.ModelForm):
	"""
	Internship form
	"""
	class Meta: # pylint: disable=R0903
		"""
		fields for intership form
		"""
		model = Internship
		fields = ['internship_id','position','pay','organization_name',
				  'organization_url', 'organization_address',
				  'supervisor_name', 'supervisor_position', 'supervisor_email',
				  'supervisor_phone']


class UpdateInternshipAssignmentForm(forms.ModelForm):
	"""
	InternshipAssignment form
	"""
	class Meta: # pylint: disable=R0903
		"""
		fields for InternshipAssignment form
		"""
		model = InternshipAssignment
		fields = ['studentid','internshipid','course_id','student_credits',
				  'semester','year','instructor','start_date','end_date']

class CreateUserForm(UserCreationForm):
	"""
	create user form
	"""
	group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
	class Meta: # pylint: disable=R0903
		"""
		fields required to create user form
		"""
		model = User
		fields = ['username', 'email','password1', 'password2', 'group']


class StudentSearchForm(forms.Form):
    """
    dropdown for fields
    """
    first_name = forms.ModelChoiceField(queryset=Student.objects.values_list(  # pylint: disable=E1101
        "first_name", flat=True).distinct(),empty_label="--------")
    last_name = forms.ModelChoiceField(queryset=Student.objects.values_list(  # pylint: disable=E1101
        "last_name", flat=True).distinct(),empty_label="--------")

    class Meta: # pylint: disable=R0903
        """
        fields for Student
        """
        model = Student
        fields = [
             "first_name",
             "last_name"
        ]


class InternshipSearchForm(forms.ModelForm):
    """
    dropdown for fields
    """
    organization_name = forms.ModelChoiceField(
        queryset=Internship.objects.values_list(  # pylint: disable=E1101
            "organization_name", flat=True).distinct(),empty_label="--------")
    supervisor_name = forms.ModelChoiceField(
        queryset=Internship.objects.values_list(  # pylint: disable=E1101
            "supervisor_name", flat=True).distinct(),empty_label="--------")


    class Meta: # pylint: disable=R0903
        """
        fields for Internship
        """
        model = Internship
        fields = ['organization_name', 'supervisor_name']


class InternshipAssignmentSearchForm(forms.ModelForm):
    """
    dropdown for fields
    """
    semester = forms.ModelChoiceField(
        queryset=InternshipAssignment.objects.values_list(  # pylint: disable=E1101
            "semester", flat=True).distinct(),empty_label="--------")
    year = forms.ModelChoiceField(
        queryset=InternshipAssignment.objects.values_list(  # pylint: disable=E1101
            "year", flat=True).distinct(),empty_label="--------")

    class Meta: # pylint: disable=R0903
        """
        fields for InternshipAssignment
        """
        model = InternshipAssignment
        fields = ['semester', 'year']
