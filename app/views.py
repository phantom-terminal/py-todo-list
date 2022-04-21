from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    context_object_name = "tasks"
    queryset = Task.objects.all().prefetch_related("tags")
    paginate_by = 10
    template_name = "app/task_list.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "app/task_confirm_delete.html"
    success_url = reverse_lazy("todo_list_app:home")


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tags"
    paginate_by = 10
    template_name = "app/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:tags")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo_list_app:tags")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "app/tag_confirm_delete.html"
    success_url = reverse_lazy("todo_list_app:tags")


def status_of_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.is_done = not task.is_done
    task.save()
    return redirect("todo_list_app:home")
