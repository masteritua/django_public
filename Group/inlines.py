from django.contrib import admin
from Student.models import Student

class StudentInline(admin.TabularInline):
    model = Student
    #after_field = Student.get_info()