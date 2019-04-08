from django.db import models
import uuid

# Create your models here.

class Event(models.Model):

    name = models.CharField(max_length=300, help_text='Enter the event name')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular event')
    fee = models.PositiveIntegerField()
    capacity  = models.PositiveIntegerField()
    target_audience = models.CharField(max_length=300)
    date = models.DateField(null = False, blank = False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    faq = models.TextField()
    tags = models.CharField(max_length=300)


    def __str__(self):
        return self.name