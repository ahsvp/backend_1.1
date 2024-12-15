from django.urls import path
from . import views

urlpatterns = [
    # Student-related URLs
    path('students/', views.get_students, name='get_students'),  # List all students
    path('students/<int:id>/', views.get_student, name='get_student'),  # Get a specific student

    # Attendance-related URLs
    path('attendance/', views.create_attendance, name='create_attendance'),  # Create attendance record
    path('attendance/<int:id>/', views.get_attendance, name='get_attendance'),  # Get a specific attendance record
    path('attendance/student/<int:student_id>/', views.get_student_attendance, name='get_student_attendance'),  # Get attendance for a specific student
]
