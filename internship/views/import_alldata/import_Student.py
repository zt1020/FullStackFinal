from internship.models import Student

def import_Student(sheet):
    last_name=sheet['A'+'2'].value
    first_name=sheet['B'+'2'].value
    major=sheet('D'+'2').value
    school_email=sheet('G'+'2').value
    major=sheet('D'+'2').value
    degree=sheet('E'+'2').value
    linkedin=sheet('H'+'2').value

    #SAVE STUDENT
    for id in ids:
        if id is not None:
            s = Student(id, unh_id,last_name,first_name,school_email,major,degree,linkedin)
            s.save()
