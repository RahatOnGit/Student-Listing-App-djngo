from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def home(request):

    query = Student.objects.all()

    context={'all_students':query}
    return render(request,'home.html',context)




def add_student(request):

    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        roll = data.get('roll')
        dept = data.get('dept')
       
        address = data.get('address')

        Student.objects.create(
            name = name, roll = roll, department = dept,
             address = address
        )

        return redirect('home')

    context={}
    return render(request,'add_student_form.html',context)


def update_student(request,pk):
    student1 = Student.objects.get(id=pk)

    if request.method == "POST":
        data = request.POST
        name = data.get('name')
        roll = data.get('roll')
        dept = data.get('dept')
        address = data.get('address')
        
        student1.name = name
        student1.roll = roll
        student1.dept = dept
        student1.address = address
        

        student1.save()
        return redirect('home')

  

    context={'student1': student1}
    return render(request,'update.html',context)

def delete_student(request,pk):
   
   student1 = Student.objects.get(id=pk)

   context={'student1': student1}
   return render(request,'middle_delete.html',context)


def delete_ok(request,pk):
   
   student1 = Student.objects.get(id=pk)
   student1.delete()

   return redirect('home')

