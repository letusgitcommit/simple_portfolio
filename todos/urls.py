from django.urls import path

from .views import (
    TodoListView,
    TodoDetailView,
    TodoCreateView,
    TodoUpdateView,
)

app_name = 'todos'

urlpatterns = [
    path('', TodoListView.as_view(), name='list'),
    path('<uuid:pk>/', TodoDetailView.as_view(), name='detail'),
    path('new-todo/', TodoCreateView.as_view(), name='new_todo'),
    path('<uuid:pk>/update-todo', TodoUpdateView.as_view(), name='update_todo')
]
