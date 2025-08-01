from django.db import models
from emp_app.models import Employee
# Create your models here.

class attendance(models.Model):
    employee = models.ForeignKey(Employee , on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.employee.first_name} - {self.date} - {self.status}"

LEAVE_STATUS = [
    ('Pending', 'Pending'),
    ('Approved', 'Approved'),
    ('Rejected', 'Rejected'),
]

LEAVE_CATEGORIES = [
    ('Casual', 'Casual'),
    ('Sick', 'Sick'),
    ('Paid', 'Paid'),
    ('Unpaid', 'Unpaid'),
    ('Other', 'Other'),
]

class leave(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    category = models.CharField(max_length=20, choices=LEAVE_CATEGORIES, default='Other')
    status = models.CharField(max_length=10, choices=LEAVE_STATUS, default='Pending')

    def __str__(self):
        return f"{self.employee.first_name} | {self.category} | {self.status}"
