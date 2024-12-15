from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100, verbose_name="Student Name")
    date_of_birth = models.DateField(verbose_name="Date of Birth")
    parent_name = models.CharField(max_length=100, verbose_name="Parent Name")
    register_number = models.CharField(max_length=50, unique=True, verbose_name="Register Number")

    def __str__(self):
        return f"{self.name} ({self.register_number})"

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="attendance_records")
    date = models.DateField(verbose_name="Date")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, verbose_name="Attendance Status")

    def __str__(self):
        return f"{self.student.name} - {self.date} - {self.status}"
