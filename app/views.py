# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import Task, Payroll, Timesheet
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from datetime import datetime

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('home') 
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
def home(request):
    # Retrieve tasks along with their associated schedule information
    tasks_with_schedule = []
    tasks = Task.objects.all()
    for task in tasks:
        schedule = task.schedule_task.first()
        if schedule:
            tasks_with_schedule.append({
                'task': task,
                'end_time': schedule.end_time,
            })

    context = {
        'tasks_with_schedule': tasks_with_schedule,
    }
    return render(request, 'home.html', context)

from django.contrib import messages

from decimal import Decimal

from django.shortcuts import get_object_or_404

@login_required
def update_task_status(request, task_id):
    # Retrieve the task object
    task = get_object_or_404(Task, pk=task_id)

    if request.method == 'POST':
        # Get the new status from the form
        new_status = request.POST.get('status')

        # Check if the new status is different from the current status
        if new_status != task.status:
            # Update the task status
            task.status = new_status
            task.save()

            # Check if the task status is completed
            if task.status == 'completed':
                # Calculate total hours worked for the task
                total_hours_worked = (task.schedule_task.first().end_time - task.schedule_task.first().start_time).total_seconds() / 3600
                
                # Calculate amount to pay the user (assuming 50% of the task amount)
                amount_to_pay = Decimal(task.amount) * Decimal('0.5') 
                
                # Create a Timesheet instance for the employee
                timesheet = Timesheet.objects.create(
                    employee=request.user,
                    date=datetime.now().date(),
                    hours_worked=total_hours_worked
                )

                # Create a Payroll instance for the employee
                payroll = Payroll.objects.create(
                    employee=request.user,
                    date=datetime.now().date(),
                    salary=amount_to_pay
                )

                # Set success message
                messages.success(request, f'Task status updated successfully. Timesheet and Payroll created. You have been paid {amount_to_pay} for this task.')
            else:
                # Set success message
                messages.success(request, 'Task status updated successfully.')
        else:
            # Set info message if status is not changed
            messages.info(request, 'Task status remains the same.')

        # Redirect back to the home page
        return redirect('home')
    else:
        # Set error message for invalid method
        messages.error(request, 'Invalid request method.')
        # Redirect back to the home page
        return redirect('home')


def view_timesheet(request):
    # Fetch timesheets for the current user
    timesheets = Timesheet.objects.filter(employee=request.user)
    context = {
        'timesheets': timesheets,
    }
    return render(request, 'timesheet.html', context)

def view_payroll(request):
    # Fetch payrolls for the current user
    payrolls = Payroll.objects.filter(employee=request.user)
    context = {
        'payrolls': payrolls,
    }
    return render(request, 'payroll.html', context)

def task_details(request, task_id):
    task = Task.objects.get(pk=task_id)
    context = {
        'task': task,
    }
    return render(request, 'task_details.html', context)
