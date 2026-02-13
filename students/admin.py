from django.contrib import admin
from django.utils.html import format_html
from .models import Student, Session, AttendanceLog, AuditLog, Badge, StudentBadge


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['university_id', 'name', 'email', 'attendance_percentage', 'total_points', 'qr_code_preview', 'created_at']
    list_filter = ['created_at', 'attendance_percentage']
    search_fields = ['university_id', 'name', 'email']
    readonly_fields = ['uuid', 'qr_code_preview', 'created_at', 'updated_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('university_id', 'name', 'email', 'phone')
        }),
        ('QR Code', {
            'fields': ('uuid', 'qr_code', 'qr_code_preview')
        }),
        ('Statistics', {
            'fields': ('attendance_percentage', 'total_points')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def qr_code_preview(self, obj):
        if obj.qr_code:
            return format_html('<img src="{}" width="100" height="100" />', obj.qr_code.url)
        return "No QR Code"
    qr_code_preview.short_description = 'QR Code Preview'
    
    actions = ['regenerate_qr_codes']
    
    def regenerate_qr_codes(self, request, queryset):
        for student in queryset:
            student.generate_qr_code()
            student.save()
        self.message_user(request, f"QR codes regenerated for {queryset.count()} students.")
    regenerate_qr_codes.short_description = "Regenerate QR codes for selected students"


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'session_type', 'date', 'start_time', 'end_time', 'location']
    list_filter = ['session_type', 'date']
    search_fields = ['title', 'location', 'description']
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Session Information', {
            'fields': ('title', 'session_type', 'date', 'start_time', 'end_time', 'location', 'description')
        }),
        ('Geo-Fencing (Optional)', {
            'fields': ('latitude', 'longitude', 'geo_fence_radius'),
            'classes': ('collapse',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    readonly_fields = ['created_at', 'updated_at']


@admin.register(AttendanceLog)
class AttendanceLogAdmin(admin.ModelAdmin):
    list_display = ['student', 'session', 'status', 'timestamp', 'recorded_by']
    list_filter = ['status', 'timestamp', 'session__session_type']
    search_fields = ['student__name', 'student__university_id', 'session__title']
    date_hierarchy = 'timestamp'
    readonly_fields = ['timestamp']
    
    fieldsets = (
        ('Attendance Information', {
            'fields': ('student', 'session', 'status', 'recorded_by', 'notes')
        }),
        ('Location Data', {
            'fields': ('scan_latitude', 'scan_longitude'),
            'classes': ('collapse',)
        }),
        ('Timestamp', {
            'fields': ('timestamp',)
        }),
    )


@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ['action_type', 'user', 'description', 'ip_address', 'timestamp']
    list_filter = ['action_type', 'timestamp']
    search_fields = ['user', 'description', 'ip_address']
    date_hierarchy = 'timestamp'
    readonly_fields = ['action_type', 'user', 'description', 'ip_address', 'timestamp']
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    list_display = ['icon', 'name', 'badge_type', 'points_required', 'color']
    list_filter = ['badge_type']
    search_fields = ['name', 'description']


@admin.register(StudentBadge)
class StudentBadgeAdmin(admin.ModelAdmin):
    list_display = ['student', 'badge', 'awarded_at']
    list_filter = ['badge', 'awarded_at']
    search_fields = ['student__name', 'student__university_id', 'badge__name']
    date_hierarchy = 'awarded_at'
    readonly_fields = ['awarded_at']
