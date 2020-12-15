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
    unh_id = models.CharField("UNH_id", unique = True, blank = False, max_length=15)
    last_name = models.CharField("Last Name", max_length=255, blank = True)
    first_name = models.CharField("First Name", max_length=255, blank = True)
    school_email = models.EmailField("School Email", max_length=255,blank = True)
    major = models.CharField("Major Name", max_length=255,null=True)
    degree = models.CharField("Degree Name", max_length=255,blank = True)
    linkedin = models.CharField("LinkedIn Profile", max_length=255,blank = True)

    def __str__(self):
        sid=self.student_id
        return str(sid)


class Internship(models.Model):
    """
    Internship data model
    """
    internship_id = models.AutoField(primary_key = True)
    position = models.CharField("Internship Position", max_length = 50)
    pay = models.CharField("Pay", max_length = 7,null=True)
    organization_name = models.CharField("Organization", max_length = 255)
    organization_url = models.CharField("URL", max_length = 255,null=True)
    organization_address = models.CharField("Mailing Address",max_length = 255)
    supervisor_name = models.CharField("Supervisor Name", max_length = 255)
    supervisor_position = models.CharField("Supervisor Position" ,max_length = 255,null=True)
    supervisor_email = models.CharField("Supervisor Email", max_length = 255,null=True)
    supervisor_phone = models.CharField("Supervisor Phone", max_length = 100,null=True)

    def __str__(self):
        iid=self.internship_id
        return str(iid)


class InternshipAssignment(models.Model):
    """
    InternshipAssignment data model
    """

    studentid = models.ForeignKey(
        Student,db_column='student_id',
        on_delete=models.CASCADE,null=True
    )
    internshipid = models.ForeignKey(
        Internship,db_column="internship_id",
        on_delete=models.CASCADE,null=True
    )
    course_id = models.CharField(
        "Course ID", max_length = 50, default = 'COMP805',null=True
    )
    student_credits = models.CharField(
        "student credits", max_length = 10, default = 3, null=True
    )
    semester = models.CharField("Semester", max_length = 30)
    year = models.CharField("Year", max_length = 10)
    instructor = models.CharField("Instructor", max_length = 40)
    start_date = models.DateField("Start Date")
    end_date = models.DateField("End Date")


    def __str__(self):
        instructor_name=self.instructor
        return str(instructor_name)
