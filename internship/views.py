from openpyxl import load_workbook
from django.http import HttpResponse
from django.shortcuts import render
#from internship.models.Student import Student
from internship.models import Student,Internship,InternshipAssignment
import xlsxwriter
from faker import Faker

w_data = xlsxwriter.Workbook("new_data.xlsx")
s_data = w_data.add_worksheet()

s_data.write("A1","Last Name")
s_data.write("B1","First Name")
s_data.write("C1","Student ID")
s_data.write("D1","Major Name")
s_data.write("E1","Degree Name")
s_data.write("F1","Phone Number")
s_data.write("G1","School Email")
s_data.write("H1","LinkedIn Profile")
s_data.write("I1","Course ID")
s_data.write("J1","Credits")
s_data.write("K1","Semester")
s_data.write("L1","Year")
s_data.write("M1","Instructor")
s_data.write("N1","Internship Position")
s_data.write("O1","Pay")
s_data.write("P1","Start Date")
s_data.write("Q1","End Date")
s_data.write("R1","Organization")
s_data.write("S1","URL")
s_data.write("T1","Mailing Address")
s_data.write("U1","City")
s_data.write("V1","State")
s_data.write("W1","City, State Zip")
s_data.write("X1","Supervisor Name")
s_data.write("Y1","Supervisor Position")
s_data.write("Z1","Supervisor Email")
s_data.write("AA1","Supervisor Phone")

f_data = Faker()

# def generate_data(f_data):
#     name = f_data.name()
#     email = f_data.email()
#     ssn = f_data.ssn()
#     phone_number = f_data.phone_number()
#     address = f_data.address()
#     return name, email, ssn, phone_number, address
#
# for i in range (0,1000):
#     name, email, ssn, phone_number, address = generate_data(f_data)
#     s_data.write(i, 0, name)
#     s_data.write(i, 1, email)
#     s_data.write(i, 2, ssn)
#     s_data.write(i, 3, phone_number)
#     s_data.write(i, 4, address)


w_data.close()


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

    for i in range(2, 115):
        last_name=sheet['A'+str(i)].value
        first_name=sheet['B'+str(i)].value
        major=sheet['D'+str(i)].value
        school_email=sheet['G'+str(i)].value
        unh_id=school_email[:6]
        degree=sheet['E'+str(i)].value
        linkedin=sheet['H'+str(i)].value


        s = Student(unh_id=unh_id,last_name=last_name,first_name=first_name, school_email=  school_email, major = major, degree=  degree, linkedin = linkedin)
        s.save()


def import_internship(sheet):

    for i in range(2, 115):
        position=sheet['N'+str(i)].value
        pay=sheet['O'+str(i)].value
        organization_name=sheet['R'+str(i)].value
        organization_url=sheet['S'+str(i)].value
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


    for i in range(2, 115):
        course_id=sheet['I'+str(i)].value
        credits=sheet['J'+str(i)].value
        semester=sheet['K'+str(i)].value
        year=sheet['L'+str(i)].value
        instructor=sheet['M'+str(i)].value
        start_date=sheet['P'+str(i)].value
        end_date=sheet['Q'+str(i)].value

        i_a = InternshipAssignment(course_id=course_id,credits=credits,
        semester=semester,year=year,instructor=instructor,start_date=start_date,end_date=end_date)
        i_a.save()
