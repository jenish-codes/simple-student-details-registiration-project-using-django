from operator import mod
from django.db import models
from students.models.departments import Department

languages = (
    ('Tamil','Tamil'),
    ('English','English'),
    ('Hindi','Hindi'),
)

class Student(models.Model):
    name  = models.CharField(max_length=60, default='')
    marks = models.IntegerField()
    dob = models.DateField()
    mother_tongue = models.CharField(max_length=100, choices=languages, default='Tamil')
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']