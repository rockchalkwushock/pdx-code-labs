from django.shortcuts import render
from .models import Todo


def index(request):
    context = {'todos': Todo.objects.all()}
    return render(request, 'todosapp/index.html', context)
