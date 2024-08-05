from django.shortcuts import render, get_object_or_404
from .models import Student, Attendance, Teacher
from .serializer import AttendanceSerializer
from .permissions import IsTeacher
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics


def attendance_log(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    attendance_records = Attendance.objects.filter(student=student).order_by("date")
    context = {"student": student, "attendance_records": attendance_records}
    return render(request, "attendance/attendance_log.html", context)


class mark_attendance(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated, IsTeacher]
