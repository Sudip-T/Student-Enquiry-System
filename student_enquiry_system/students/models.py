from django.db import models
from courses.models import CourseModel



class StudentModel(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=120)
    current_degree = models.CharField(max_length=20, null=True, blank=True)
    profile_img = models.FileField(upload_to='profiles/', null=True, blank=True)
    courses = models.ForeignKey(CourseModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Students Model'
        verbose_name_plural = 'StudentsModel'

    def __str__(self):
        return self.first_name
