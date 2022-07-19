from django.contrib import admin
from .models import Student, Department


class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'marks', 'dob', 'department']

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Student, StudentAdmin)
admin.site.register(Department, DepartmentAdmin)
