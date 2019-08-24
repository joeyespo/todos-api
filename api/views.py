from json import loads

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods, require_safe

from . import serializers
from .models import Todo


@require_safe
def index(request):
    base_url = request.build_absolute_uri().rstrip('/')
    return JsonResponse({
        'todos_url': f'{base_url}/todos',
        'todo_url': f'{base_url}/todos/{{id}}',
        'complete_url': f'{base_url}/{{id}}/complete',
    })


@require_safe
def todos(request):
    # TODO: Sorting (created_at by default), other filters, etc
    todos = Todo.objects.filter(completed=False).all()

    if request.method == 'POST':
        # TODO: Implement bulk update
        return JsonResponse({})

    return JsonResponse(serializers.todos(todos))


@require_http_methods(['HEAD', 'GET', 'POST'])
def todo(request, id):
    if request.method == 'POST':
        data = loads(request.body)
        todo, created = Todo.objects.get_or_create(id=id, defaults={
            'text': data['text'],
        })
    else:
        todo = get_object_or_404(Todo, pk=id)

    return JsonResponse(serializers.todo(todo))


@require_http_methods(['HEAD', 'POST'])
def complete_todo(request, id):
    todo = get_object_or_404(Todo, pk=id)
    todo.completed = True
    todo.save()
    return JsonResponse(serializers.todo(todo))
