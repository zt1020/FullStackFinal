"""
admin.py
Contributors: Snehitha, harshani
"""
from django.contrib import admin
#from internship.models.Student import Student
from internship.models import Student,Internship,InternshipAssignment
admin.site.register(Student)
admin.site.register(Internship)
admin.site.register(InternshipAssignment)
