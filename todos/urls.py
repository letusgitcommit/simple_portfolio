from django.urls import path

from .views import TodoListView, TodoDetailView

app_name = 'todos'

urlpatterns = [
    path('', TodoListView.as_view(), name='list'),
    path('<uuid:pk>/', TodoDetailView.as_view(), name='detail'),
]
