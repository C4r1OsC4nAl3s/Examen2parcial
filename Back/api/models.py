from django.db import models
from django.contrib.auth.models import User
from datetime import date

CHOICES_STATUS = {
    "DONE": "Finished",
    "PEND": "Pending",
    "UNDO": "Unodone",
}

class Task(models.Model):
    title = models.CharField(max_length=80, default="title")
    description = models.CharField(max_length=250, default="description")
    created_at = models.DateField(default=date.today, blank=True, null=False)
    due_date = models.DateField(default=date.today, blank=True, null=False)
    status = models.CharField(max_length=4, choices=CHOICES_STATUS)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title