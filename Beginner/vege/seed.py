from faker import Faker
fake = Faker()

import random
from .models import *
from django.db.models import Sum

# Creating fake data 

def create_subject_marks() -> None:

    try:
        student_objs = Student.objects.all()

        for student in student_objs:
            subject_objs = Subject.objects.all()

            for subject in subject_objs:

                SubjectMarks.objects.create(
                    student=student,
                    subject=subject,
                    marks=random.randint(0, 100)
                )
        
    except Exception as e:
        print("Error while creating subject marks:", e)    

# This function will return nothing similar to void in C++
def seed_db(n=10) -> None:
    
    try:
        for _ in range(n):
            # [0,2,4,5] department objects
            department_objs = Department.objects.all()
            random_index = random.randint(0, len(department_objs)-1)

            department = department_objs[random_index]
            student_id = f'STU-0{random.randint(100, 999)}'
            student_name = fake.name()
            student_email = fake.email()
            student_age = random.randint(20,30)
            student_address = fake.address()

            student_id_obj = StudentID.objects.create(student_id=student_id)

            student_obj = Student.objects.create(   
                department=department,
                student_id=student_id_obj,
                student_name=student_name,
                student_email=student_email,
                student_age=student_age,
                student_address=student_address
            )
        

    except Exception as e:
        print("Error while seeding the database:", e)    


def generate_report_card():

    # current_rank = -1
    ranks = Student.objects.annotate(total_marks=Sum('studentmarks__marks')).order_by('-total_marks')

    i = 1
    
    for rank in ranks:
        ReportCard.objects.create(
            student=rank,
            student_rank=i
        )
        i+=1
