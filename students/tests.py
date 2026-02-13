from django.test import TestCase, Client
from django.urls import reverse
from .models import Student, Session, AttendanceLog, Badge
from datetime import date


class StudentModelTest(TestCase):
    """Test cases for Student model"""
    
    def setUp(self):
        self.student = Student.objects.create(
            university_id="TEST001",
            name="Test Student",
            email="test@example.com"
        )
    
    def test_student_creation(self):
        """Test student is created with UUID and QR code"""
        self.assertIsNotNone(self.student.uuid)
        self.assertEqual(self.student.name, "Test Student")
        self.assertEqual(self.student.attendance_percentage, 0)
    
    def test_qr_code_generation(self):
        """Test QR code is generated for student"""
        self.assertIsNotNone(self.student.qr_code)
        self.assertTrue(self.student.qr_code.name.startswith('qr_codes/qr_'))


class SessionModelTest(TestCase):
    """Test cases for Session model"""
    
    def setUp(self):
        self.session = Session.objects.create(
            title="Test Lecture",
            session_type="lecture",
            date=date.today(),
            location="Room 101"
        )
    
    def test_session_creation(self):
        """Test session is created correctly"""
        self.assertEqual(self.session.title, "Test Lecture")
        self.assertEqual(self.session.session_type, "lecture")
        self.assertEqual(self.session.location, "Room 101")


class AttendanceLogTest(TestCase):
    """Test cases for AttendanceLog model"""
    
    def setUp(self):
        self.student = Student.objects.create(
            university_id="TEST001",
            name="Test Student",
            email="test@example.com"
        )
        self.session = Session.objects.create(
            title="Test Lecture",
            session_type="lecture",
            date=date.today()
        )
    
    def test_attendance_log_creation(self):
        """Test attendance log is created"""
        log = AttendanceLog.objects.create(
            student=self.student,
            session=self.session,
            status='present'
        )
        self.assertEqual(log.status, 'present')
        self.assertEqual(log.student, self.student)
        self.assertEqual(log.session, self.session)
    
    def test_unique_student_session(self):
        """Test that student-session combination is unique"""
        AttendanceLog.objects.create(
            student=self.student,
            session=self.session,
            status='present'
        )
        # Attempting to create duplicate should fail
        with self.assertRaises(Exception):
            AttendanceLog.objects.create(
                student=self.student,
                session=self.session,
                status='late'
            )


class ViewsTest(TestCase):
    """Test cases for views"""
    
    def setUp(self):
        self.client = Client()
        self.student = Student.objects.create(
            university_id="TEST001",
            name="Test Student",
            email="test@example.com"
        )
    
    def test_home_view(self):
        """Test home page loads correctly"""
        response = self.client.get(reverse('students:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Smart Student Management System')
    
    def test_student_list_view(self):
        """Test student list page loads correctly"""
        response = self.client.get(reverse('students:student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Student')
    
    def test_student_detail_view(self):
        """Test student detail page loads correctly"""
        response = self.client.get(reverse('students:student_detail', args=[self.student.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Test Student')
    
    def test_dashboard_view(self):
        """Test dashboard page loads correctly"""
        response = self.client.get(reverse('students:dashboard'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Admin Dashboard')
    
    def test_scanner_view(self):
        """Test scanner page loads correctly"""
        response = self.client.get(reverse('students:scanner'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'QR Code Scanner')
