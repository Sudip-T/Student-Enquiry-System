from django.contrib import admin
from .models import CourseModel


class CourseModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', 'code')


admin.site.register(CourseModel, CourseModelAdmin)
