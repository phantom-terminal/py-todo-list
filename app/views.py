from django.urls import reverse_lazy
from django.views import generic

from app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = "app/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('todo_list_app:home')


class TagListView(generic.ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = "app/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy('todo_list_app:tags')
