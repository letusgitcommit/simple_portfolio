from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TodoCreateModelForm
from .models import Todo


class TodoListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoDetailView(LoginRequiredMixin, generic.DetailView):
    context_object_name = 'todo'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)
