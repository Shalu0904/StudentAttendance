from django.contrib import admin
from .models import Student, Attendance, Teacher
from .forms import AttendanceForm
from django.utils import timezone


def MarkTodaysAttendance(modeladmin, request, queryset):
    today = timezone.now().date()
    for student in queryset:
        attendance, created = Attendance.objects.get_or_create(
            student=student, date=today, defaults={"present": True}
        )
        if not created:
            attendance.present = True
            attendance.save()


MarkTodaysAttendance.short_description = "Mark today's attendance for selected students"


class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "email", "date_of_birth", "phone_number"]
    search_fields = ["first_name", "last_name", "email"]
    actions = [MarkTodaysAttendance]


class AttendanceAdmin(admin.ModelAdmin):
    form = AttendanceForm
    list_display = ["student", "date", "present"]
    list_filter = ["date", "present"]
    search_fields = ["student_first_name", "student_last_name"]


admin.site.register(Student, StudentAdmin)
admin.site.register(Attendance, AttendanceAdmin)
admin.site.register(Teacher)
