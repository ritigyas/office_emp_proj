from django.urls import path
from . import views

urlpatterns = [
    path('', views.payroll_dashboard, name='payroll_dashboard'),
    path('view-breakup/', views.view_salary_breakup, name='view_salary_breakup'),
    path('credit-salary/', views.credit_salary, name='credit_salary'),
    path('payslip-history/', views.payslip_history, name='payslip_history'),
]
