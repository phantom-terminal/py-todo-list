from django.urls import path
from .views import TaskListView, TagListView, TaskCreateView, TagCreateView

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tags/create/", TagCreateView.as_view(), name="tags_create"),
]

app_name = "todo_list_app"
