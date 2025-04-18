from django.shortcuts import render,redirect
from .models import Todo

# Create your views here.
def todo_list(request):
    if request.method == 'POST':
        #getting the data from the client
        title = request.POST.get('title')
        description = request.POST.get('description')
        completed = request.POST.get('completed') == 'on'
        due_date = request.POST.get('due_date')

        # Save the new todo to the database
        todo = Todo(
            title=title,
            description=description,
            completed=completed,
            due_date=due_date
        )
        todo.save() # Save the new todo to the database and compulsary to write this line
        return redirect('todo_list')   # Redirect to avoid form resubmission
    todos = Todo.objects.all().order_by('-due_date')
    return render(request, 'todo_list.html',{'todos': todos})

