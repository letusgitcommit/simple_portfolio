from django import forms
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import TodoCreateModelForm, TodoUpdateModelForm
from .models import Todo


class TodoListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


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
