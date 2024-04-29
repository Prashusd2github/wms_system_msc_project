# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register_view, name='register'),
    path('', views.task_list, name='task_list'),
    path('schedule/', views.view_schedule, name='view_schedule'),
    path('payroll/', views.view_payroll, name='view_payroll'),
    path('timesheet/', views.view_timesheet, name='view_timesheet'),
    path('update_task_status/<int:task_id>/', views.update_task_status, name='update_task_status'),
]