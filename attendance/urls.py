from django.urls import path
from .views import attendance_log
from .views import mark_attendance

urlpatterns = [
    path("attendance_log/<int:student_id>/", attendance_log, name="attendance_log"),
    path('mark-attendance/', mark_attendance.as_view(), name='mark_attendance'),


  
  


]
