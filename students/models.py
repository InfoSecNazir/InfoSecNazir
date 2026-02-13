import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models
from django.utils import timezone
from PIL import Image


class Student(models.Model):
    """Student model with unique UUID for QR code generation"""
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    university_id = models.CharField(max_length=50, unique=True, verbose_name="University ID")
    name = models.CharField(max_length=200, verbose_name="Student Name")
    email = models.EmailField(unique=True, verbose_name="Email Address")
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Phone Number")
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True, verbose_name="QR Code")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Gamification fields
    total_points = models.IntegerField(default=0, verbose_name="Total Points")
    attendance_percentage = models.DecimalField(max_digits=5, decimal_places=2, default=0.00, verbose_name="Attendance %")
    
    class Meta:
        ordering = ['name']
        verbose_name = "Student"
        verbose_name_plural = "Students"
    
    def __str__(self):
        return f"{self.name} ({self.university_id})"
    
    def generate_qr_code(self):
        """Generate QR code for the student based on their UUID"""
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr_data = f"STUDENT:{self.uuid}"
        qr.add_data(qr_data)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save QR code to file
        buffer = BytesIO()
        img.save(buffer, format='PNG')
        file_name = f'qr_{self.university_id}.png'
        self.qr_code.save(file_name, File(buffer), save=False)
        buffer.close()
    
    def save(self, *args, **kwargs):
        # Generate QR code on first save or if it doesn't exist
        if not self.qr_code:
            super().save(*args, **kwargs)  # Save first to get an ID
            self.generate_qr_code()
            kwargs['force_insert'] = False  # Prevent duplicate key error
        super().save(*args, **kwargs)


class Session(models.Model):
    """Session model for tracking lectures, labs, exams, etc."""
    SESSION_TYPES = [
        ('lecture', 'Lecture'),
        ('lab', 'Laboratory'),
        ('exam', 'Exam'),
        ('assignment', 'Assignment Submission'),
        ('other', 'Other'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="Session Title")
    session_type = models.CharField(max_length=20, choices=SESSION_TYPES, default='lecture', verbose_name="Type")
    date = models.DateField(default=timezone.now, verbose_name="Date")
    start_time = models.TimeField(blank=True, null=True, verbose_name="Start Time")
    end_time = models.TimeField(blank=True, null=True, verbose_name="End Time")
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name="Location")
    description = models.TextField(blank=True, null=True, verbose_name="Description")
    
    # Geo-fencing fields
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Latitude")
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Longitude")
    geo_fence_radius = models.IntegerField(default=100, verbose_name="Geo-fence Radius (meters)")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date', '-start_time']
        verbose_name = "Session"
        verbose_name_plural = "Sessions"
    
    def __str__(self):
        return f"{self.title} - {self.date} ({self.get_session_type_display()})"


class AttendanceLog(models.Model):
    """Attendance log model for tracking student attendance and task submissions"""
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('excused', 'Excused'),
        ('submitted', 'Submitted'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_logs')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='attendance_logs')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='present', verbose_name="Status")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Recorded At")
    
    # Geo-location fields
    scan_latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Scan Latitude")
    scan_longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name="Scan Longitude")
    
    # Audit fields
    recorded_by = models.CharField(max_length=100, blank=True, null=True, verbose_name="Recorded By")
    notes = models.TextField(blank=True, null=True, verbose_name="Notes")
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Attendance Log"
        verbose_name_plural = "Attendance Logs"
        unique_together = ['student', 'session']
    
    def __str__(self):
        return f"{self.student.name} - {self.session.title} - {self.get_status_display()}"


class AuditLog(models.Model):
    """Audit log for tracking system actions"""
    ACTION_TYPES = [
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
        ('scan', 'QR Scan'),
        ('export', 'Data Export'),
        ('import', 'Data Import'),
    ]
    
    action_type = models.CharField(max_length=20, choices=ACTION_TYPES, verbose_name="Action Type")
    user = models.CharField(max_length=100, verbose_name="User")
    description = models.TextField(verbose_name="Description")
    ip_address = models.GenericIPAddressField(blank=True, null=True, verbose_name="IP Address")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Timestamp")
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Audit Log"
        verbose_name_plural = "Audit Logs"
    
    def __str__(self):
        return f"{self.action_type} by {self.user} at {self.timestamp}"


class Badge(models.Model):
    """Badge model for gamification"""
    BADGE_TYPES = [
        ('attendance', 'Attendance'),
        ('punctuality', 'Punctuality'),
        ('submission', 'Assignment Submission'),
        ('excellence', 'Excellence'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Badge Name")
    badge_type = models.CharField(max_length=20, choices=BADGE_TYPES, verbose_name="Type")
    description = models.TextField(verbose_name="Description")
    icon = models.CharField(max_length=50, default='🏆', verbose_name="Icon/Emoji")
    points_required = models.IntegerField(default=0, verbose_name="Points Required")
    color = models.CharField(max_length=20, default='gold', verbose_name="Color")
    
    class Meta:
        verbose_name = "Badge"
        verbose_name_plural = "Badges"
    
    def __str__(self):
        return f"{self.icon} {self.name}"


class StudentBadge(models.Model):
    """Many-to-many relationship between students and badges"""
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='badges')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE, related_name='awarded_to')
    awarded_at = models.DateTimeField(auto_now_add=True, verbose_name="Awarded At")
    
    class Meta:
        unique_together = ['student', 'badge']
        ordering = ['-awarded_at']
        verbose_name = "Student Badge"
        verbose_name_plural = "Student Badges"
    
    def __str__(self):
        return f"{self.student.name} - {self.badge.name}"
