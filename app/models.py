from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)

class Task(models.Model):
    TASK_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    load = models.IntegerField(default= 0)

    def _str_(self):
        return self.title

class Schedule(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='schedule_task')
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedules')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __str__(self):
        return f"{self.employee.username} - Schedule"

class Timesheet(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='timesheets')
    date = models.DateField()
    hours_worked = models.DecimalField(max_digits=5, decimal_places=2)
    
    def _str_(self):
        return f"{self.employee.user.username} - {self.date}"

class Payroll(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payrolls')
    date = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    
    def _str_(self):
        return f"{self.employee.user.username} - {self.month.strftime('%B %Y')}"


