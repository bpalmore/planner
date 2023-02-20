from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request):
    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/')

    todos = Todo.objects.all()
    return render(
        request,
        'index.html',
        {
            "todos": todos,
        }
    )

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')
