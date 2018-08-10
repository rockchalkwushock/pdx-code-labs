from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Todo


def index(request):
    context = {'todos': Todo.objects.all().order_by('-created_date')[:5]}
    return render(request, 'todosapp/index.html', context)


def add(request):
    if request.method == 'POST':
        todo_text = request.POST['todoInput']
        new_todo = Todo(todo_text=todo_text)
        new_todo.save()
        return HttpResponseRedirect(reverse('todos:index'))


def complete(request):
    if request.method == 'POST':
        todo_text = request.POST['todo']
        selected_todo = Todo.objects.get(todo_text=todo_text)
        if selected_todo.completed:
            selected_todo.completed = False
        else:
            selected_todo.completed = True
        selected_todo.save()
    return HttpResponseRedirect(reverse('todos:index'))


def delete(request):
    if request.method == 'POST':
        todo_text = request.POST['todo']
        selected_todo = Todo.objects.get(todo_text=todo_text)
        selected_todo.delete()
    return HttpResponseRedirect(reverse('todos:index'))
