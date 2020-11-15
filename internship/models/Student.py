"""
models.py
Harshani, Snehitha
Updated : 11/10/2020
"""
from django.db import models


class Student(models.Model):
    """
    student data model
    """
    student_id=models.AutoField(primary_key=True)
    unh_id = models.CharField("UNH ID", blank = False, max_length=11)
    last_name = models.CharField("Last Name", max_length=255)
    first_name = models.CharField("First Name", max_length=255)
    school_email = models.EmailField("School Email", max_length=255)
    major = models.CharField("Major Name", max_length=255)
    degree = models.CharField("Degree Name", max_length=255)
    linkedin = models.CharField("LinkedIn Profile", max_length=255)


    def __str__(self):
       name=self.last_name+self.first_name
       return name


class Internship(models.Model):
    """
    Internship data model
    """
    internship_id = models.AutoField(primary_key = True)
    position = models.CharField("Internship Position", max_length = 50)
    pay = models.CharField("Pay", max_length = 7)
    organization_name = models.CharField("Organization", max_length = 255)
    organization_url = models.CharField("URL", max_length = 255)
    organization_address = models.CharField("Mailing Address",max_length = 255)
    supervisor_name = models.CharField("Supervisor Name", max_length = 255)
    supervisor_position = models.CharField("Supervisor Position" ,max_length = 255)
    supervisor_email = models.CharField("Supervisor Email", max_length = 255)
    supervisor_phone = models.CharField("Supervisor Phone", max_length = 15)

    def __str__(self):
       company_name=self.organization_name
       return company_name


class InternshipAssignment(models.Model):
    """
    InternshipAssignment data model
    """
    id=models.AutoField(primary_key=True)
    studentid = models.ForeignKey(Student,db_column='student_id',on_delete=models.CASCADE,default=1,null=True)
    internshipid = models.ForeignKey(Internship,db_column="internship_id",on_delete=models.CASCADE,null=True)
    course_id = models.CharField("Course ID", max_length = 10)
    credits = models.CharField("Credits", max_length = 1)
    semester = models.CharField("Semester", max_length = 7)
    year = models.CharField("Year", max_length = 4)
    instructor = models.CharField("Instructor", max_length = 15)
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")


    def __str__(self):
       instructor_name=self.instructor
       return instructor_name
