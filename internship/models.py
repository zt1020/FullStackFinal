"""
models.py
Harshani, Snehitha
Updated : 11/10/2020
"""
from django.db import models
from model_utils.models import TimeStampedModel

class Student(TimeStampedModel):
    """
    student data model
    """
    student_id = models.AutoField("Student ID", primary_key = True)
    unh_id = models.CharField("UNH ID", blank = False, max_length=11)
    last_name = models.CharField("Last Name", max_length=255)
    first_name = models.CharField("First Name", max_length=255)
    school_email = models.EmailField("School Email", max_length=255)
    major = models.CharField("Major Name", max_length=255)
    degree = models.CharField("Degree Name", max_length=255)
    linkedin = models.CharField("LinkedIn Profile", max_length=255)


class Internship(TimeStampedModel):
    """
    Internship data model
    """
    internship_id = models.AutoField("Internship ID", primary_key = True)
    position = models.CharField("Internship Position", max_length = 50)
    pay = models.CharField("Pay", max_length = 7)
    organization_name = models.CharField("Organization", max_length = 255)
    organization_url = models.CharField("URL", max_length = 255)
    organization_address = models.CharField("Mailing Address",max_length = 255)
    supervisor_name = models.CharField("Supervisor Name", max_length = 255)
    supervisor_position = models.CharField("Supervisor Position" ,max_length = 255)
    supervisor_email = models.CharField("Supervisor Email", max_length = 255)
    supervisor_phone = models.CharField("Supervisor Phone", max_length = 15)


class InternshipAssignment(TimeStampedModel):
    """
    InternshipAssignment data model
    """
    student_id = models.ForeignKey(Student, verbose_name = 'Student ID', \
    on_delete=models.CASCADE)
    internship_id = models.ForeignKey(Internship, \
    verbose_name = 'Internship ID', on_delete=models.CASCADE)
    course_id = models.CharField("Course ID", max_length = 10)
    credits = models.CharField("Credits", max_length = 1)
    semester = models.CharField("Semester", max_length = 7)
    year = models.CharField("Year", max_length = 4)
    instructor = models.CharField("Instructor", max_length = 15)
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")
