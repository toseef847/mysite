from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from .models import Todo
from datetime import datetime

# list All the todo(s)
def todo_list(request):
    todos = Todo.objects.all().order_by('id')
    context = {
        'todos': todos
    }
    return render(request, 'todo/index.html', context)

# Display single list
def todo(request, todo_id):
    todo = get_object_or_404(Todo, pk= todo_id)
    context = {
        'todo': todo
    }
    return render(request, 'todo/view.html', context)

# Create a new todo
def create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        todo = Todo(title = title, description = description)
        todo.save()
        return redirect('todo:todo_list')
    else:
        return render(request, 'todo/create.html')

# Update a todo
def updateform(request, todo_id):
    if todo_id is not None:
        todo = get_object_or_404(Todo, pk = todo_id)
        if todo_id:
            context = {
                'todo': todo
            }
        return render(request, 'todo/update.html', context)

def update(request, todo_id):
    title = request.POST['title']
    description = request.POST['description']

    if request.POST.get('completed', "false") == 'on':
        done = True
    else:
        done = False
    Todo.objects.filter(pk=todo_id).update(title= title, description= description, completed = done)
    return redirect('todo:todo_list')

# Confirm Delettion before deleting
def ConfirmDelete(request, todo_id):
    if todo_id is not None:
        todo = get_object_or_404(Todo, pk = todo_id)
        if todo_id:
            context = {
                'todo': todo,
            }
        return render(request, 'todo/delete.html', context)

# Delete a todo
def delete(request, todo_id):
    todo = Todo.objects.get(pk = todo_id)
    todo.delete()
    return redirect('todo:todo_list')
