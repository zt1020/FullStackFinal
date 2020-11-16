"""
views.py
Contributors: Harshani, Snehitha
Updated : 11/16/2020
"""

from openpyxl import load_workbook
# from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
# import xlsxwriter
from faker import Faker
from internship.models import Student,Internship,InternshipAssignment

f_data = Faker()

def import_file(request):
    """
    import the file
    """
    if request.method=='POST':
        file = request.FILES['document']
        import_data(file)
    return render(request, 'import.html')

def import_data(request):
    """
    loads the workbook and write functions to import the data
    """
    work_book = load_workbook(filename = request, data_only=True)
    sheet = work_book['sample-internship-data']
    import_student(sheet)
    import_internship(sheet)
    import_internshipassignment(sheet)

def import_student(sheet):
    """
    importing student and generating fake data
    """
    for i in range(2, 10):
        student_id=str(i-1)
        last_name=f_data.last_name()
        first_name=f_data.first_name()
        major=sheet['D'+str(i)].value
        school_email=f_data.email()
        unh_id=school_email[:6]
        degree=sheet['E'+str(i)].value
        linkedin=f_data.url()

        import_s = Student(
            student_id=student_id,
            unh_id=unh_id,last_name=last_name,first_name=first_name,
            school_email=  school_email, major = major,
            degree=  degree, linkedin = linkedin
        )
        import_s.save()

def import_internship(sheet):
    """
    importing internship and generating fake data
    """
    for i in range(2, 10):

        # internship_id=str(i-1)
        position=sheet['N'+str(i)].value
        pay=sheet['O'+str(i)].value
        organization_name=sheet['R'+str(i)].value
        organization_url=f_data.url()
        organization_address=sheet['T'+str(i)].value
        supervisor_name=sheet['X'+str(i)].value
        supervisor_position=sheet['Y'+str(i)].value
        supervisor_email=sheet['Z'+str(i)].value
        supervisor_phone=sheet['AA'+str(i)].value


        import_i = Internship(
            position=position,
            pay=pay,
            organization_name=organization_name,
            organization_url=organization_url,
            organization_address=organization_address,
            supervisor_name=supervisor_name,
            supervisor_position=supervisor_position,
            supervisor_email=supervisor_email,
            supervisor_phone=supervisor_phone
        )
        import_i.save()

def import_internshipassignment(sheet):
    """
    importing InternshipAssignment and generating fake data
    """
    for i in range(2, 10):

        course_id=sheet['I'+str(i)].value
        student_credits=sheet['J'+str(i)].value
        semester=sheet['K'+str(i)].value
        year=sheet['L'+str(i)].value
        instructor=sheet['M'+str(i)].value
        start_date=f_data.date()
        end_date=f_data.date()

        import_ia = InternshipAssignment(
            course_id=course_id,student_credits=student_credits,
            semester=semester,
            year=year,
            instructor=instructor,
            start_date=start_date,end_date=end_date
        )
        import_ia.save()


class HomepageView(TemplateView):
    """
    This creates class based HomepageView
    """
    template_name = 'home.html'
