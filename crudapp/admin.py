from django.contrib import admin
from django.db import models
from crudapp.models import Student, subject

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']

@admin.register(subject)
class subjectAdmin(admin.ModelAdmin):
    list_display = ['stu_id','CourseName','credithours']
