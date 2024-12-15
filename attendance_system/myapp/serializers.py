from rest_framework import serializers
from .models import Student, Attendance

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'date_of_birth', 'parent_name', 'register_number']

class AttendanceSerializer(serializers.ModelSerializer):
    student = StudentSerializer()  # Nested StudentSerializer for student details

    class Meta:
        model = Attendance
        fields = ['id', 'student', 'date', 'status']

class CreateAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['student', 'date', 'status']
