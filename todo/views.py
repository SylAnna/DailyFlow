from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from .forms import ListForm
from .services import TaskService, CalendarService


# Initialize services
task_service = TaskService()
calendar_service = CalendarService()

def home(request):
    """renders the home page of the app"""
    return render(request, 'index.html')


def todos(request):
    """handles the todo-list page"""
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Item Has Been Added To List!")
            return redirect('todos')
    else:
        form = ListForm()

    all_items = task_service.get_all_tasks()
    task_today = task_service.get_tasks_for_today()

    return render(request, 'todos.html', {
        'form': form,
        'all_items': all_items,
        'tasks': task_today
    })


def delete(request, list_id):
    """deletes a specific task from the todo-list"""
    task_service.delete_task(list_id)
    messages.success(request, "Item has been deleted")
    return redirect('todos')


def cross_off(request, list_id):
    """cross off task when marked completed"""
    task_service.mark_completed(list_id, True)
    return redirect('todos')


def uncross(request, list_id):
    """uncross task when not completed"""
    task_service.mark_completed(list_id, False)
    return redirect('todos')


def edit(request, list_id):
    """displays edit page for handling updating the task"""
    item = task_service.get_task_by_id(list_id)
    if request.method == 'POST':
        item_name = request.POST.get('item')
        completed = request.POST.get('completed') == 'True'
        task_service.update_task(list_id, item_name, completed)
        messages.success(request, "Item has been updated!")
        return redirect('todos')
    else:
        return render(request, 'edit.html', {'item': item})


def calendar(request):
    """renders the calendar page with task displayed"""
    tasks = task_service.get_all_tasks()
    
    return render(request, 'calendar.html', {
        'tasks': tasks
    })
