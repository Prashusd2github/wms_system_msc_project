# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Task, Schedule, Timesheet, Payroll, Employee
from .forms import UserForm
from django.http import JsonResponse
from .utils import generate_employee_id
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('task_list')  # Redirect to your home page after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def task_list(request):
    assigned_tasks = Task.objects.filter(assigned_to=request.user)
    context = {
        'assigned_tasks': assigned_tasks,
    }
    return render(request, 'tasks/task_list.html', context)

def view_schedule(request):
    # Fetch schedule for the current user
    schedules = request.user.schedules.all()
    context = {
        'schedules': schedules,
    }
    return render(request, 'tasks/view_schedule.html', context)

def view_payroll(request):
    # Fetch payroll for the current user
    payrolls = request.user.payrolls.all()
    context = {
        'payrolls': payrolls,
    }
    return render(request, 'tasks/view_payroll.html', context)

def view_timesheet(request):
    # Fetch timesheets for the current user
    timesheets = request.user.timesheets.all()
    context = {
        'timesheets': timesheets,
    }
    return render(request, 'tasks/view_timesheet.html', context)

def update_task_status(request, task_id):
    if request.method == 'POST':
        # Retrieve the task object
        task = Task.objects.get(pk=task_id)
        # Update the task status
        new_status = request.POST.get('status')
        task.status = new_status
        task.save()
        # Return JSON response indicating success
        return JsonResponse({'success': True})
    else:
        # Return JSON response indicating failure
        return JsonResponse({'success': False})