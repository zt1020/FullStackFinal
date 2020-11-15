from openpyxl import load_workbook
from django.http import HttpResponse
from django.shortcuts import render
#from internship.models.Student import Student
from internship.models.Student import Student,Internship,InternshipAssignment

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


    last_name=sheet['A'+'2'].value
    first_name=sheet['B'+'2'].value
    major=sheet['D'+'2'].value
    school_email=sheet['G'+'2'].value
    unh_id=school_email[:6]
    degree=sheet['E'+'2'].value
    linkedin=sheet['H'+'2'].value


    s = Student(unh_id=unh_id,last_name=last_name,first_name=first_name, school_email=  school_email, major = major, degree=  degree, linkedin = linkedin)
    s.save()


def import_internship(sheet):

    position=sheet['N'+'2'].value
    pay=sheet['O'+'2'].value
    organization_name=sheet['R'+'2'].value
    organization_url=sheet['S'+'2'].value
    organization_address=sheet['T'+'2'].value
    supervisor_name=sheet['X'+'2'].value
    supervisor_position=sheet['Y'+'2'].value
    supervisor_email=sheet['Z'+'2'].value
    supervisor_phone=sheet['AA'+'2'].value


    i = Internship(position=position,pay=pay,organization_name=organization_name,
    organization_url=organization_url,organization_address=organization_address,supervisor_name=supervisor_name,
    supervisor_position=supervisor_position,supervisor_email=supervisor_email,
    supervisor_phone=supervisor_phone)
    i.save()




def import_internshipAssignment(sheet):
    
    course_id=sheet['I'+'2'].value
    credits=sheet['J'+'2'].value
    semester=sheet['K'+'2'].value
    year=sheet['L'+'2'].value
    instructor=sheet['M'+'2'].value
    start_date=sheet['P'+'2'].value
    end_date=sheet['Q'+'2'].value



    i_a = InternshipAssignment(course_id=course_id,credits=credits,
    semester=semester,year=year,instructor=instructor,start_date=start_date,end_date=end_date)
    i_a.save()
