from django.db import models
from django.contrib.auth.models import User 
# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('todo', 'To Do'),
        ('done', 'Done'),
        ('notdone', 'Not Done'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='todo')

    class Meta:
        db_table = 'task'
        managed = False

    def __str__(self):
        return self.title