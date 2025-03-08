# management/forms.py
from django import forms
from .models import Department, Student

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['Did','Dname' ]
        widgets = {
            'Did': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter department id '
            }),
            'Dname': forms.TextInput(attrs={
                'class': 'form-control',
                
                'placeholder': 'Enter department name'
            }),
        }
            



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['roll_no', 'name', 'cgpa', 'department', 'marksheet']
        widgets = {
            'roll_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter roll number'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                
                'placeholder': 'Enter student\'s name'
            }),
            'cgpa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter CGPA'
            }),
            'department': forms.Select(attrs={
                'class': 'form-control'
            }),
            'marksheet': forms.FileInput(attrs={
                'class': 'form-control'
            }),
        }

