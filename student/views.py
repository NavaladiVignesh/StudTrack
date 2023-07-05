from django.shortcuts import redirect, render
from student.models import Student
from student.db.dbconnection import test_connection

def std(request):
    print(request)
    if request.method == "POST":
        id = request.POST['id']
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        student =  Student.objects.create(studentId=id,studentName=name,studentEmail=email,studentContact=contact)
        print(student)
        if(test_connection()): student.save()
        return redirect('list')
    return render(request,"index.html")

def read_data(request):
    if(test_connection()): students = Student.objects.filter()
    return render(request,"show.html",{"students":students})

def destroy(request,id):
    if(test_connection()):
        student = Student.objects.get(id=id)
        student.delete()
    return redirect('list')

def edit(request,id):
    if(test_connection()):
        student = Student.objects.get(id=id)
        student.delete()
    return redirect('std')