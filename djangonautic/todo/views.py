from django.shortcuts import redirect, render
from .models import Todo
from .forms import TodoForm, TodoModelForm
from django.views.decorators.http import require_POST


def index(request):
    todos = Todo.objects.order_by('id')

    # form = TodoForm()
    form = TodoModelForm()
    context = {
        'todos': todos,
        'form': form
    }
    return render(request, 'todo/index.html', context)


@require_POST
def addTodo(request):
    form = TodoModelForm(request.POST or None)
    if form.is_valid():
        # todo = Todo(text=request.POST['text'])
        form.save()

    return redirect('index')


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')

