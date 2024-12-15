from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from .models import Student, Attendance
from django.utils import timezone

class StudentModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="John Doe",
            date_of_birth="2000-01-01",
            parent_name="Jane Doe",
            register_number="REG12345"
        )

    def test_student_creation(self):
        self.assertEqual(self.student.name, "John Doe")
        self.assertEqual(self.student.date_of_birth, "2000-01-01")
        self.assertEqual(self.student.parent_name, "Jane Doe")
        self.assertEqual(self.student.register_number, "REG12345")

    def test_string_representation(self):
        self.assertEqual(str(self.student), "John Doe (REG12345)")

class AttendanceModelTest(TestCase):
    def setUp(self):
        self.student = Student.objects.create(
            name="John Doe",
            date_of_birth="2000-01-01",
            parent_name="Jane Doe",
            register_number="REG12345"
        )
        self.attendance = Attendance.objects.create(
            student=self.student,
            date=timezone.now().date(),
            status="Present"
        )

    def test_attendance_creation(self):
        self.assertEqual(self.attendance.student.name, "John Doe")
        self.assertEqual(self.attendance.status, "Present")

    def test_attendance_string_representation(self):
        self.assertEqual(str(self.attendance), f"John Doe - {self.attendance.date} - Present")

class StudentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student_data = {
            "name": "Jane Smith",
            "date_of_birth": "2001-02-02",
            "parent_name": "John Smith",
            "register_number": "REG67890"
        }

    def test_create_student(self):
        response = self.client.post("/api/students/", self.student_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.student_data['name'])
        self.assertEqual(response.data['register_number'], self.student_data['register_number'])

    def test_get_students(self):
        self.client.post("/api/students/", self.student_data, format='json')
        response = self.client.get("/api/students/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

class AttendanceAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.student = Student.objects.create(
            name="John Doe",
            date_of_birth="2000-01-01",
            parent_name="Jane Doe",
            register_number="REG12345"
        )
        self.attendance_data = {
            "student": self.student.id,
            "date": "2024-11-16",
            "status": "Present"
        }

    def test_create_attendance(self):
        response = self.client.post("/api/attendance/", self.attendance_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['status'], self.attendance_data['status'])

    def test_get_attendance(self):
        self.client.post("/api/attendance/", self.attendance_data, format='json')
        response = self.client.get("/api/attendance/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
