from tkinter import Widget
from django import forms
from django.forms import ModelForm
from students.models.students import Student


class AddStudent(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'dob': forms.TextInput(attrs={'type':'date'}),
        }
