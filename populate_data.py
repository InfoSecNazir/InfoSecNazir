#!/usr/bin/env python
"""Script to populate the database with sample data"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ssms_project.settings')
django.setup()

from students.models import Student, Session, AttendanceLog, Badge
from django.utils import timezone
from datetime import datetime, timedelta

print("Creating sample students...")

# Create students
students_data = [
    {"university_id": "CS2021001", "name": "Ahmad Hassan", "email": "ahmad.hassan@university.edu"},
    {"university_id": "CS2021002", "name": "Fatima Ali", "email": "fatima.ali@university.edu"},
    {"university_id": "CS2021003", "name": "Mohammed Khalil", "email": "mohammed.khalil@university.edu"},
    {"university_id": "CS2021004", "name": "Sara Ibrahim", "email": "sara.ibrahim@university.edu"},
    {"university_id": "CS2021005", "name": "Omar Nasser", "email": "omar.nasser@university.edu"},
]

students = []
for data in students_data:
    student, created = Student.objects.get_or_create(
        university_id=data["university_id"],
        defaults=data
    )
    if created:
        print(f"Created student: {student.name}")
    students.append(student)

print("\nCreating sample sessions...")

# Create sessions
today = timezone.now().date()
sessions_data = [
    {
        "title": "Introduction to Programming",
        "session_type": "lecture",
        "date": today - timedelta(days=7),
        "location": "Room 101"
    },
    {
        "title": "Data Structures Lab",
        "session_type": "lab",
        "date": today - timedelta(days=5),
        "location": "Lab 202"
    },
    {
        "title": "Algorithms Lecture",
        "session_type": "lecture",
        "date": today - timedelta(days=3),
        "location": "Room 103"
    },
    {
        "title": "Midterm Exam",
        "session_type": "exam",
        "date": today - timedelta(days=1),
        "location": "Hall A"
    },
    {
        "title": "Database Design",
        "session_type": "lecture",
        "date": today,
        "location": "Room 105"
    },
]

sessions = []
for data in sessions_data:
    session, created = Session.objects.get_or_create(
        title=data["title"],
        date=data["date"],
        defaults=data
    )
    if created:
        print(f"Created session: {session.title}")
    sessions.append(session)

print("\nCreating sample attendance records...")

# Create attendance records
import random
statuses = ['present', 'late', 'absent']
for session in sessions[:-1]:  # All but today's session
    for student in students:
        # Random attendance with bias towards present
        status = random.choices(statuses, weights=[7, 2, 1])[0]
        log, created = AttendanceLog.objects.get_or_create(
            student=student,
            session=session,
            defaults={
                'status': status,
                'recorded_by': 'admin'
            }
        )
        if created:
            print(f"  {student.name} - {session.title}: {status}")

# Update attendance percentages
print("\nUpdating attendance percentages...")
for student in students:
    total_sessions = AttendanceLog.objects.filter(student=student).count()
    attended = AttendanceLog.objects.filter(
        student=student,
        status__in=['present', 'late']
    ).count()
    if total_sessions > 0:
        student.attendance_percentage = (attended / total_sessions) * 100
        student.save()
        print(f"  {student.name}: {student.attendance_percentage:.1f}%")

print("\nCreating sample badges...")

# Create badges
badges_data = [
    {
        "name": "Perfect Attendance",
        "badge_type": "attendance",
        "description": "Achieved 100% attendance",
        "icon": "🏆",
        "points_required": 100,
        "color": "gold"
    },
    {
        "name": "Early Bird",
        "badge_type": "punctuality",
        "description": "Never late to class",
        "icon": "⏰",
        "points_required": 50,
        "color": "blue"
    },
    {
        "name": "Assignment Master",
        "badge_type": "submission",
        "description": "Submitted all assignments on time",
        "icon": "📚",
        "points_required": 75,
        "color": "green"
    },
]

for data in badges_data:
    badge, created = Badge.objects.get_or_create(
        name=data["name"],
        defaults=data
    )
    if created:
        print(f"Created badge: {badge.name}")

print("\n✅ Sample data created successfully!")
print(f"   Students: {Student.objects.count()}")
print(f"   Sessions: {Session.objects.count()}")
print(f"   Attendance Records: {AttendanceLog.objects.count()}")
print(f"   Badges: {Badge.objects.count()}")
