from django.db import models


class CourseModel(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)

    class Meta:
        db_table = 'Courses Model'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name
 