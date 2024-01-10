from django.db import models
from django.contrib.auth.models import User


class TODO(models.Model):
    '''
    Defining Our Todo Model class here
    '''

    # Defining Choices for Status and Priority
    task_status_choices = [
        ('C', 'Mark as Completed'),
        ('P', 'Pending'),
    ]
    task_priorties_choice = [
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low')
    ]
    title = models.CharField(max_length=50)
    status = models.CharField(
        max_length=2, choices=task_status_choices, default='P')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(max_length=2, choices=task_priorties_choice)
