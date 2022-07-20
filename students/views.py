from atexit import register
from django.shortcuts import redirect, render
from django.views import View

from students.models import students
from .models import Student
from students.forms import AddStudent



class Home(View):
    def get(self, request):
        form = AddStudent()
        return render(request, "students/index.html", {'form':form})
    
    def post(self, request):
        form = AddStudent(request.POST)
        if form.is_valid():
            form.save()
        return redirect('details')



def details(request):
    students = Student.objects.all()
    return render(request, "students/details.html", {'students': students})



class Update(View):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        form = AddStudent(instance=student)
        context = {
            'student' : student,
            'form' : form,
        }
        return render(request, "students/update.html", context)

    def post(self, request, id):
        student = Student.objects.get(id=id)
        form = AddStudent(request.POST, instance=student)
        if form.is_valid():
            form.save()
        return redirect("details")


class Delete(View):
    def get(self, request, id):
        student = Student.objects.get(id=id)
        form = AddStudent(instance=student)
        context = {
            'student' : student,
            'form' : form,
        }
        return render(request, "students/delete.html", context)

    def post(self, request, id):
        student = Student.objects.get(id=id)
        student.delete()
        return redirect("details")