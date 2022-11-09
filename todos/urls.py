from django.urls import path

from .views import (
    TodoListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
    SubtaskCreateView,
    TodoDeleteView,
)

app_name = 'todos'

urlpatterns = [
    path('', TodoListView.as_view(), name='list'),
    path('<uuid:pk>/', TodoDetailView.as_view(), name='detail'),
    path('new-todo/', TodoCreateView.as_view(), name='new_todo'),
    path('<uuid:pk>/update-todo', TodoUpdateView.as_view(), name='update_todo'),
    path('<uuid:parent_pk>/new-subtask/', SubtaskCreateView.as_view(), name='new_subtask'),
    path('<uuid:pk>/delete-todo/', TodoDeleteView.as_view(), name='delete_todo'),
]
