# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/register/', views.register_view, name='register'),
    path('', views.task_list, name='task_list'),
    # path('schedules/<int:employee_id>/', views.employee_schedule, name='employee_schedule'),
    # path('timesheets/<int:employee_id>/', views.employee_timesheets, name='employee_timesheets'),
    # path('payrolls/<int:employee_id>/', views.employee_payroll, name='employee_payroll'),
]