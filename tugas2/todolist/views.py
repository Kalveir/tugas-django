from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from .models import Todo

def index(request):
	all_todos = Todo.objects.all()
	context = dict(
		todos = all_todos
	)
	return render(request, 'todolist/index.html', context)

def add(request):
	new_todo = request.POST['todo']
	todo = Todo(text = new_todo)
	todo.save()

	return HttpResponseRedirect(reverse('todo-index'))

# Create your views here.
