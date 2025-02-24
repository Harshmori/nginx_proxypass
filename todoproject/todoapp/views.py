from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Todo

def todo_list(request):
    todos = Todo.objects.all().order_by('-created_date')
    return render(request, 'todoapp/todo_list.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title:
            Todo.objects.create(title=title, description=description)
            messages.success(request, 'Todo added successfully!')
        return redirect('todo_list')
    return render(request, 'todoapp/add_todo.html')

def delete_todo(request, pk):
    Todo.objects.get(pk=pk).delete()
    messages.success(request, 'Todo deleted successfully!')
    return redirect('todo_list')

def complete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()
    return redirect('todo_list')