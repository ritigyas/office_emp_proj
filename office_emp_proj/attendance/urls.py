# attendance/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.attendance_home, name='attendance_home'),
    path('report/', views.employee_report_view, name='employee_report'),
    path('org-report/', views.organization_report_view, name='organization_report'),
    path('mark-attendance/', views.mark_attendance_page, name='mark_attendance_page'),
    path('apply-leave/', views.apply_leave_page, name='apply_leave_page'),
    path('manage-leaves/', views.manage_leaves, name='manage-leaves'),  # ✅ FIXED HERE
    path('org-leave-report/', views.org_leave_report, name='org-leave-report'),
]
