from django.db import models
from django.forms import ModelForm, Textarea
from django.contrib import admin

class CourseDetails(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    faculty = models.CharField(max_length=100, blank=True)
    pre_requisites = models.CharField(max_length=300, blank=True)
    start_date = models.DateField()
    end_date = models.DateField()
    
class StudentDetail(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100, blank=True)
    marital_status = models.CharField(max_length=100, blank=True)
    profession = models.CharField(max_length=100, blank=True)
    education = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=300, blank=True)
    churned = models.BooleanField(max_length=100, blank=True)

class StudentCourses(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    courses = models.ForeignKey(CourseDetails, on_delete=models.CASCADE)