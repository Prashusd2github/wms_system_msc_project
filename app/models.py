from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=20, unique=True)
    # password = models.CharField(max_length=50, default=None)
    def _str_(self):
        return self.user.username

class Task(models.Model):
    TASK_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks')
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def _str_(self):
        return self.title

class Schedule(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='schedule_task')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedules')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    def _str_(self):
        return f"{self.employee.user.username} - {self.date}"

class Timesheet(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='timesheets')
    date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    
    def _str_(self):
        return f"{self.employee.user.username} - {self.date}"

class Payroll(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payrolls')
    month = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def _str_(self):
        return f"{self.employee.user.username} - {self.month.strftime('%B %Y')}"