from django.urls import path
from .views import (
    TaskListView,
    TagListView,
    TaskCreateView,
    TagCreateView,
    TaskUpdateView,
    TagUpdateView,
    TagDeleteView,
    TaskDeleteView,
    status_of_task,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update", TaskUpdateView.as_view(), name="task_update"),
    path("task/<int:pk>/delete", TaskDeleteView.as_view(), name="task_delete"),
    path("task/<int:pk>/", status_of_task, name="task_status_change"),
    path("tags/", TagListView.as_view(), name="tags"),
    path("tags/create/", TagCreateView.as_view(), name="tags_create"),
    path("tags/<int:pk>/update", TagUpdateView.as_view(), name="tags_update"),
    path("tags/<int:pk>/delete", TagDeleteView.as_view(), name="tags_delete"),
]

app_name = "todo_list_app"
