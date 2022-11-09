from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from uuid import uuid4

user_model = get_user_model()


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    text = models.TextField()
    complete = models.BooleanField(default=False)
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    parent_task = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    created_timestamp = models.DateTimeField(auto_now_add=True)
    modified_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:15] + '...'

    def get_absolute_url(self):
        return reverse('todos:detail', kwargs={'pk': self.pk})

