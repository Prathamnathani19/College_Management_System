from django.urls import path
from management.views import *

urlpatterns = [
    path('', ulogin, name='ulogin'),
    path('signup/', usignup, name='usignup'),
    path('home/', uhome, name='uhome'),
    path('logout/', logout_view, name='logout'),
    path('departments/', department_list, name='department_list'),
    path('departments/add/', add_department, name='add_department'),
    path('departments/edit/<int:Did>/', department_edit, name='department_edit'),
    path('departments/delete/<int:Did>/', delete_department, name='delete_department'),
    path('students/', student_list, name='student_list'),
    path('students/add/', add_student, name='add_student'),
    path('students/edit/<int:roll_no>/', student_edit, name='student_edit'),
    path('students/delete/<int:roll_no>/', delete_student, name='delete_student'),
]
