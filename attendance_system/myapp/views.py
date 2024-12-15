from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student, Attendance
from .serializers import StudentSerializer, AttendanceSerializer
from django.shortcuts import get_object_or_404

# View to retrieve all students
@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# View to retrieve a specific student by ID
@api_view(['GET'])
def get_student(request, id):
    student = get_object_or_404(Student, id=id)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

# View to create a new student
@api_view(['POST'])
def create_student(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to retrieve all attendance records
@api_view(['GET'])
def get_attendance(request):
    attendance = Attendance.objects.all()
    serializer = AttendanceSerializer(attendance, many=True)
    return Response(serializer.data)

# View to create a new attendance record
@api_view(['POST'])
def create_attendance(request):
    serializer = AttendanceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# View to retrieve attendance for a specific student by student ID
@api_view(['GET'])
def get_student_attendance(request, student_id):
    attendances = Attendance.objects.filter(student_id=student_id)
    serializer = AttendanceSerializer(attendances, many=True)
    return Response(serializer.data)

# View to retrieve a specific attendance record by ID
@api_view(['GET'])
def get_attendance_by_id(request, id):
    attendance = get_object_or_404(Attendance, id=id)
    serializer = AttendanceSerializer(attendance)
    return Response(serializer.data)
