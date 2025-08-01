from django.db import models
from attendance.models import Employee
from django.utils import timezone

class SalaryBreakup(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    basic = models.FloatField()
    hra = models.FloatField()
    income_tax = models.FloatField()
    deductions = models.FloatField()
    gross_salary = models.FloatField()
    net_salary = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Salary breakup for {self.employee.first_name} {self.employee.last_name}"

class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_breakup = models.ForeignKey(SalaryBreakup, on_delete=models.CASCADE)
    date_credited = models.DateField(default=timezone.now)

    def __str__(self):
        return f"Payslip: {self.employee.first_name} on {self.date_credited}"
