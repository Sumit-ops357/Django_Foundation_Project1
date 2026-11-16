from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Subject)


class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']


admin.site.register(SubjectMarks, SubjectMarksAdmin)   

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student', 'student_rank', 'date_created']
    ordering = ['student_rank']


admin.site.register(ReportCard, ReportCardAdmin)