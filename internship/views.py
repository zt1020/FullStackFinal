from openpyxl import load_workbook
from django.http import HttpResponse
from django.shortcuts import render
#from internship.models.Student import Student
from internship.models import Student,Internship,InternshipAssignment
import xlsxwriter
from faker import Faker


f_data = Faker()

def import_file(request):
    if request.method=='POST':
        file = request.FILES['document']
        import_data(file)
    return render(request, 'import.html')

def import_data(request):
    wb = load_workbook(filename = request, data_only=True)
    sheet = wb['sample-internship-data']
    import_Student(sheet)
    import_internship(sheet)
    import_internshipAssignment(sheet)

def import_Student(sheet):

    for i in range(2, 10):

        student_id=str(i-1)
        last_name=f_data.last_name()
        first_name=f_data.first_name()
        major=sheet['D'+str(i)].value
        school_email=f_data.email()
        unh_id=school_email[:6]
        degree=sheet['E'+str(i)].value
        linkedin=f_data.url()


        s = Student(student_id=student_id,\
        unh_id=unh_id,last_name=last_name,first_name=first_name, school_email=  school_email, major = major, degree=  degree, linkedin = linkedin)
        s.save()


def import_internship(sheet):

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


        i = Internship(position=position,pay=pay,organization_name=organization_name,
        organization_url=organization_url,organization_address=organization_address,supervisor_name=supervisor_name,
        supervisor_position=supervisor_position,supervisor_email=supervisor_email,
        supervisor_phone=supervisor_phone)
        i.save()




def import_internshipAssignment(sheet):


    for i in range(2, 10):

        course_id='COMP805'
        credits='3'
        semester=sheet['K'+str(i)].value
        year=sheet['L'+str(i)].value
        instructor=sheet['M'+str(i)].value
        start_date=f_data.date()
        end_date=f_data.date()

        i_a = InternshipAssignment(course_id=course_id,credits=credits,
        semester=semester,year=year,instructor=instructor,start_date=start_date,end_date=end_date)
        i_a.save()
