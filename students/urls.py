from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('students/<int:student_id>/', views.student_detail, name='student_detail'),
    path('scanner/', views.scanner_interface, name='scanner'),
    path('api/scan/', views.process_qr_scan, name='process_scan'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('export/excel/', views.export_attendance_excel, name='export_excel'),
    path('sessions/', views.session_list, name='session_list'),
    path('sessions/<int:session_id>/', views.session_detail, name='session_detail'),
]
