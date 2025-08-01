# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import attendance , leave
from emp_app.models import Employee
import json
from django.contrib.auth.decorators import login_required

def attendance_home(request):
    return render(request, 'attendance/attendance_home.html')


def index(request):
    return HttpResponse("Welcome to the Attendance app!")

# def mark_attendance_api(request):
#     if request.method=='POST':
#         data = json.loads(request.body)
#         emp_id = data['emp_id']
#         date = data['date']
#         status = data['status']
#         try:
#             emp = Employee.objects.get(emp_id=emp_id)
#             attendance.objects.create(employee = emp , date = date , status = status)
#             return JsonResponse({'messgae':'Attendace marked'} , status = 200)
#         except Employee.DoesNotExist:
#             return JsonResponse({'error':'invalid employee id'} , status = 400)
#     return JsonResponse({'error': 'Invalid method'}, status=405)  

# def apply_leave_api(request):
#     if request.method=='POST':
#         data = json.loads(request.body)
#         emp_id = data.get('emp_id')
#         employee = Employee.objects.get(id=emp_id)
#         leave.objects.create(
#             employee = employee,
#             start_date = data.get('start_date'),
#             end_date = data.get('end_date'),
#             reason = data.get('reason')
#         )
#         return JsonResponse({'message':'Leave applied'} , status = 201)

@login_required
def employee_report_view(request):
    user = request.user

    try:
        employee = user.employee
    except AttributeError:
        return render(request , "attendance/error.html" , {"message" :  "employee profile not linked."})
    
    attendance_records = attendance.objects.filter(employee = employee)
    leave_records = leave.objects.filter(employee = employee)

    context = {
        "employee" : employee ,
        "attendance_records" : attendance_records,
        "leave_records" : leave_records,
    }

    return render(request , 'attendance/employee_report.html' , context)

from django.db.models import Count
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def organization_report_view(request):
    # Total attendance days per employee
    attendance_summary = (
        attendance.objects.values('employee__first_name')
        .annotate(total_days=Count('id'))
        .order_by('-total_days')
    )

    # Total leaves per employee
    leave_summary = (
        leave.objects.values('employee__first_name')
        .annotate(total_leaves=Count('id'))
        .order_by('-total_leaves')
    )

    context = {
        "attendance_summary": attendance_summary,
        "leave_summary": leave_summary,
    }
    return render(request, "attendance/org_report.html", context)


from datetime import date
from django.contrib import messages

def mark_attendance_page(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        status = request.POST.get('status', 'Present')  # or take from form

        try:
            emp = Employee.objects.get(id =emp_id)
            today = date.today()

            # Avoid marking attendance twice
            if not attendance.objects.filter(employee=emp, date=today).exists():
                attendance.objects.create(employee=emp, date=today, status=status)
                messages.success(request, "Attendance marked successfully.")
            else:
                messages.warning(request, "Attendance already marked for today.")
        except Employee.DoesNotExist:
            messages.error(request, "Invalid employee ID.")

        return render(request, 'attendance/mark_attendance.html')

    return render(request, 'attendance/mark_attendance.html')


from django.contrib import messages
from emp_app.models import Employee
from .models import leave

def apply_leave_page(request):
    if request.method == 'POST':
        emp_id = request.POST.get('emp_id')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        reason = request.POST.get('reason')

        try:
            employee = Employee.objects.get(id=emp_id)
            leave.objects.create(
                employee=employee,
                start_date=start_date,
                end_date=end_date,
                reason=reason
            )
            messages.success(request, "Leave applied successfully.")
        except Employee.DoesNotExist:
            messages.error(request, "Invalid Employee ID.")

    return render(request, 'attendance/apply_leave.html')


from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from .models import leave

def is_admin(user):
    return user.is_authenticated and user.is_superuser  # or user.is_staff for staff-only

@user_passes_test(is_admin)
@login_required
def manage_leaves(request):
    all_leaves = leave.objects.all()

    if request.method == "POST":
        leave_id = request.POST.get("leave_id")
        new_status = request.POST.get("status")

        try:
            leave_obj = leave.objects.get(id=leave_id)
            leave_obj.status = new_status
            leave_obj.save()
        except leave.DoesNotExist:
            pass

        return redirect('manage-leaves')

    return render(request, 'attendance/manage_leaves.html', {'leaves': all_leaves})

def org_leave_report(request):
    leaves = leave.objects.select_related('employee').all()
    return render(request, 'attendance/org_leave_report.html', {'leaves': leaves})
