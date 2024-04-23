# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Task, Schedule, Timesheet, Payroll, Employee
from .forms import TaskForm, ScheduleForm, TimesheetForm, PayrollForm, UserForm
from .utils import generate_employee_id

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                login(request, user)
                return redirect('task_list')
            else:
                error_message = 'Invalid username or password.'
                return render(request, 'login.html', {'error_message': error_message})
        except User.DoesNotExist:
            error_message = 'Invalid username'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            employee_id = generate_employee_id()  
            employee = Employee.objects.create(user=user, employee_id=employee_id)
            return redirect('task_list')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def task_list(request):
    tasks = Task.objects.filter(assigned_to=request.user.employee)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def schedule_list(request):
    schedules = Schedule.objects.filter(employee=request.user.employee)
    return render(request, 'schedules/schedule_list.html', {'schedules': schedules})

@login_required
def timesheet_list(request):
    timesheets = Timesheet.objects.filter(employee=request.user.employee)
    return render(request, 'timesheets/timesheet_list.html', {'timesheets': timesheets})

@login_required
def payroll_list(request):
    payrolls = Payroll.objects.filter(employee=request.user.employee)
    return render(request, 'payrolls/payroll_list.html', {'payrolls': payrolls})

