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
from django.views.generic import ListView
from .models import Student, InternshipAssignment,Internship
from .forms import StudentSearchForm
from .forms import InternshipSearchForm
from .forms import InternshipAssignmentSearchForm

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
        unh_id=str(i-1)
        last_name=f_data.last_name()
        first_name=f_data.first_name()
        major=sheet['D'+str(i)].value
        school_email=f_data.email()
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

        internship_id=str(i-1)
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
            internship_id=internship_id,
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

def display_students(request):
    button = "students"
    student_items = Student.objects.all()
    form = StudentSearchForm(request.POST or None)
    first_name=Student.objects.all()
    last_name=Student.objects.all()
    context = {
        'button' : button,
        'student_items' : student_items,
        'form' : form,
        'first_name':first_name,
        'last_name':last_name
    }
    if request.method == 'POST':
        student_items = Student.objects.filter(first_name__icontains=form['first_name'].value(),
                                            last_name__icontains=form['last_name'].value()


                                          )
        context = {
            "student_items" : student_items,
            "form": form
        }
    return render(request, 'display_students.html', context)

def display_internship(request):
    button = "Internship"
    internship_items = Internship.objects.all()
    form = InternshipSearchForm(request.POST or None)
    context = {
        'button' : button,
        'internship_items' : internship_items,
        'form' : form
    }
    if request.method == 'POST':
        internship_items = Internship.objects.filter(organization_name__icontains=form['organization_name'].value(),
                                          supervisor_name__icontains=form['supervisor_name'].value()
                                          )
        context = {
            "internship_items" : internship_items,
            "form": form
        }
    return render(request, 'display_internships.html', context)

def display_internshipassignment(request):
    button = "Internship Assignment"
    internshipassignment_items = InternshipAssignment.objects.all()
    form = InternshipAssignmentSearchForm(request.POST or None)
    context = {
        'button' : button,
        'internshipassignment_items' : internshipassignment_items,
        'form' : form
    }
    if request.method == 'POST':
        internshipassignment_items = InternshipAssignment.objects.filter(semester__icontains=form['semester'].value(),
                                          year__icontains=form['year'].value()
                                          )
        context = {
            "internshipassignment_items" : internshipassignment_items,
            "form": form
        }
    return render(request, 'display_internshipassignment.html', context)
