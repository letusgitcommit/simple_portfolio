from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import Todo


class TodoCreateModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['text']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-todo_create_form'
        self.helper.form_method = 'post'
        custom_submit = Submit('submit', 'Submit Todo')
        custom_submit.field_classes = 'btn btn-success'
        self.helper.add_input(custom_submit)


class TodoUpdateModelForm(TodoCreateModelForm):
    class Meta(TodoCreateModelForm.Meta):
        fields = ['text', 'complete']
