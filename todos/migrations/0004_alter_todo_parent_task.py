# Generated by Django 4.1.3 on 2022-11-09 03:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0003_todo_created_timestamp_todo_modified_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='parent_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subtasks', to='todos.todo'),
        ),
    ]