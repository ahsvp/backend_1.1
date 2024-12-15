from django.contrib import admin
from .models import Student, Attendance

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_of_birth', 'parent_name', 'register_number')
    search_fields = ('name', 'register_number')
    list_filter = ('date_of_birth',)
    ordering = ('id',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'student', 'date', 'status')
    search_fields = ('student__name',)
    list_filter = ('date', 'status')
    ordering = ('date',)


# Register your models here.
