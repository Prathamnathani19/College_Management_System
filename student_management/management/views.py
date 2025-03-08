from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Department, Student
from .forms import DepartmentForm, StudentForm
from django.http import HttpResponse

def ulogin(request):
    if request.user.is_authenticated:
        return redirect("uhome")
    else:
        if request.method == "POST":
            un = request.POST.get("un")
            pw = request.POST.get("pw")
            usr = authenticate(username=un, password=pw)
            if usr is None:
                msg = "Login Denied."
                return render(request, "ulogin.html", {"msg": msg})
            else:
                login(request, usr)
                return redirect("uhome")
        else:
            return render(request, "ulogin.html")
def usignup(request):
    if request.user.is_authenticated:
        return redirect("uhome")
    else:
        if request.method == "POST":
            un = request.POST.get("un")
            email = request.POST.get("email")
            pw1 = request.POST.get("pw1")
            pw2 = request.POST.get("pw2")
            if pw1 == pw2:
                try:
                    usr = User.objects.get(username=un)
                    msg = "User already exists"
                    return render(request, "usignup.html", {"msg": msg})
                except User.DoesNotExist:
                    usr = User.objects.create_user(username=un, password=pw1)
                    usr.save()
                    return redirect("ulogin")
            else:
                msg = "Passwords did not match"
                return render(request, "usignup.html", {"msg": msg})
        else:
            return render(request, "usignup.html")

@login_required
def uhome(request):
    return render(request, "uhome.html")

@login_required
def logout_view(request):
    logout(request)
    return redirect("ulogin")

@login_required
def department_list(request):
    departments = Department.objects.all()
    return render(request, "department_list.html", {"departments": departments})

@login_required
def add_department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("department_list")
    else:
        form = DepartmentForm()
    return render(request, "add_department.html", {"form": form})

@login_required
def department_edit(request, Did):
    department = get_object_or_404(Department, Did=Did)
    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('department_list')
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'add_department.html', {'form': form})

@login_required
def delete_department(request, Did):
    department = get_object_or_404(Department, Did = Did)
    department.delete()
    return redirect("department_list")

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, "student_list.html", {"students": students})

@login_required
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()
    return render(request, "add_student.html", {"form": form})

@login_required
def student_edit(request, roll_no):
    student = get_object_or_404(Student, roll_no=roll_no)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_edit.html', {'form': form, 'student': student})

@login_required
def delete_student(request, roll_no):
    student = get_object_or_404(Student, roll_no=roll_no)
    student.delete()
    return redirect("student_list")
