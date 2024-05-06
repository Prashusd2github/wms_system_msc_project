from django.contrib import admin
from .models import Task, Schedule, Timesheet, Payroll, Profile

from django.contrib import admin

# Change the name of the administration site
admin.site.site_header = 'Worker Management System'

class ScheduleInline(admin.TabularInline):
    model = Schedule
    extra = 0

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'amount', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('title', 'description')
    inlines = [ScheduleInline]

class TimesheetAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'hours_worked')
    list_filter = ('employee',)
    search_fields = ('employee__username', 'date')

class PayrollAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'salary')
    list_filter = ('employee',)
    search_fields = ('employee__username', 'date')

admin.site.register(Task, TaskAdmin)
admin.site.register(Timesheet, TimesheetAdmin)
admin.site.register(Payroll, PayrollAdmin)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'hourly_rate')