from django.urls import path
from .views import attendance_log

urlpatterns = [
    path("attendance_log/<int:student_id>/", attendance_log, name="attendance_log"),
]
