from django.contrib import admin
from .models import StudentModel


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'contact', 'created_at')
    search_fields = ('first_name', 'email', 'course')


admin.site.register(StudentModel, StudentAdmin)


# customizing admin panel title and name
admin.site.site_header = 'Student Enquiry System'