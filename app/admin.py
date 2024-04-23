from django.contrib import admin
from .models import Employee, Task, Schedule, Timesheet, Payroll

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['user', 'employee_id']
    search_fields = ['user__username', 'employee_id']

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'assigned_to', 'status', 'created_at', 'updated_at']
    list_filter = ['status', 'created_at', 'updated_at']
    search_fields = ['title', 'description', 'assigned_to__user__username']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['employee', 'date', 'start_time', 'end_time']
    list_filter = ['date']
    search_fields = ['employee__user__username']

@admin.register(Timesheet)
class TimesheetAdmin(admin.ModelAdmin):
    list_display = ['employee', 'date', 'hours_worked']
    list_filter = ['date']
    search_fields = ['employee__user__username']

@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
    list_display = ['employee', 'month', 'salary']
    list_filter = ['month']
    search_fields = ['employee__user__username']
