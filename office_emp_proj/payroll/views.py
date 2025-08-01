from django.shortcuts import render, redirect
from attendance.models import Employee
from .models import SalaryBreakup, Payslip
from django.contrib import messages

from attendance.models import Employee
from .models import SalaryBreakup

def generate_salary_breakup(emp_id):
    employee = Employee.objects.get(id=emp_id)  # ✅ convert ID to actual object
    total_salary = employee.salary

    basic = total_salary * 0.50
    hra = total_salary * 0.20
    income_tax = total_salary * 0.10
    deductions = total_salary * 0.05
    gross_salary = basic + hra
    net_salary = gross_salary - income_tax - deductions

    breakup = SalaryBreakup.objects.create(
        employee=employee,
        basic=basic,
        hra=hra,
        income_tax=income_tax,
        deductions=deductions,
        gross_salary=gross_salary,
        net_salary=net_salary
    )

    return breakup


def payroll_dashboard(request):
    return render(request, 'payroll/dashboard.html')

from django.shortcuts import render, get_object_or_404
from .models import SalaryBreakup
from attendance.models import Employee

def view_salary_breakup(request):
    context = {}
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        try:
            breakup = SalaryBreakup.objects.get(employee__id=emp_id)
        except SalaryBreakup.DoesNotExist:
            try:
                breakup = generate_salary_breakup(emp_id)  # automatically creates breakup
            except Employee.DoesNotExist:
                context['error'] = "Employee does not exist."
                return render(request, 'payroll/view_breakup.html', context)

        context['breakup'] = breakup
    return render(request, 'payroll/view_breakup.html', context)

def credit_salary(request):
    if request.method == "POST":
        emp_id = request.POST.get("emp_id")
        try:
            emp = Employee.objects.get(id=emp_id)
            breakup = generate_salary_breakup(emp.id)
            Payslip.objects.create(employee=emp, salary_breakup=breakup)
            messages.success(request, f"Salary credited and payslip generated for {emp.first_name}")
        except Employee.DoesNotExist:
            messages.error(request, "Employee not found.")
    return render(request, 'payroll/credit_salary.html')

def payslip_history(request):
    payslips = Payslip.objects.select_related('employee', 'salary_breakup').order_by('-date_credited')
    return render(request, 'payroll/payslip_history.html', {'payslips': payslips})
