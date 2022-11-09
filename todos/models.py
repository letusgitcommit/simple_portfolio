from django.db import models
from django.contrib.auth import get_user_model
from uuid import uuid4

user_model = get_user_model()


class Todo(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    text = models.TextField()
    complete = models.BooleanField()
    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    parent_task = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

