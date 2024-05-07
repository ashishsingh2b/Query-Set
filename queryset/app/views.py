from django.shortcuts import render
from .models import Student
# Create your views here.

def home(request):
    #student_data = Student.objects.all()
    #student_data = Student.objects.filter(city="surat")
    #student_data = Student.objects.exclude(city="surat")
    student_data = Student.objects.exclude(city="surat")
    print("Return:",student_data)
    print()
    print("SQL Query:", student_data.query)
    return render(request,'school/home.html',{'students':student_data})