# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('accounts/register/', views.register_view, name='register'),
    path('', views.home, name='home'),
    path('update_task_status/<int:task_id>/', views.update_task_status, name='update_task_status'),
    path('timesheet/', views.view_timesheet, name='timesheet'),
    path('payroll/', views.view_payroll, name='payroll'),
    path('task/<int:task_id>/', views.task_details, name='task_details'),

]