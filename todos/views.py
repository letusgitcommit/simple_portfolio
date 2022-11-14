from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from rest_framework.viewsets import ModelViewSet

from .forms import TodoCreateModelForm, TodoUpdateModelForm
from .models import Todo
from .serializers import TodoSerializer, NewTodoSerializer, UpdateTodoSerializer

class TodoListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).filter(parent_task=None)


class TodoDetailView(LoginRequiredMixin, generic.DetailView):
    context_object_name = 'todo'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = TodoCreateModelForm
    template_name = 'todos/todo_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['text'].widget = forms.TextInput()
        return form


class TodoUpdateView(LoginRequiredMixin, generic.UpdateView):
    form_class = TodoUpdateModelForm
    template_name = 'todos/todo_form.html'
    context_object_name = 'todo'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['text'].widget = forms.TextInput()
        return form


class SubtaskCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = TodoCreateModelForm
    template_name = 'todos/todo_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.parent_task = get_object_or_404(
            Todo.objects.filter(user=self.request.user),
            pk=kwargs.get('parent_pk')
        )
        self.extra_context = {'parent_task': self.parent_task}
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.parent_task = self.parent_task
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['text'].widget = forms.TextInput()
        return form


class TodoDeleteView(LoginRequiredMixin, generic.DeleteView):
    success_url = reverse_lazy('todos:list')
    context_object_name = 'todo'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class TodoAPIModelViewSet(ModelViewSet):

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).filter(parent_task=None)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return TodoSerializer
        elif self.request.method == 'POST':
            return NewTodoSerializer
        else:
            return UpdateTodoSerializer
