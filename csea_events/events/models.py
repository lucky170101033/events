from django.db import models
import uuid

from django.contrib.auth.models import User

# Create your models here.
class Btech(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Mtech(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PhD(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):

    # todo, extend and test by sunday

    name = models.CharField(max_length=300)
    event_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular event')
    fee = models.PositiveIntegerField()
    capacity  = models.PositiveIntegerField()
    target_audience = models.CharField(max_length=300)
    date = models.DateField(null = False, blank = False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    summary = models.TextField(blank=True, null=True)
    faq = models.TextField(blank=True, null=True)
    tags = models.CharField(max_length=300, help_text=' (Press Ctrl to select multiple)')
    organisors = models.CharField(max_length=300, default='(not specified)')
    contact_info = models.CharField(max_length=300, default='(not specified)')
    # requester = models.ForeignKey(User, unique=True, on_delete=models.CASCADE, default=None)
    invitees_btech = models.ManyToManyField(Btech, help_text=' (Press Ctrl to select multiple)')
    invitees_mtech = models.ManyToManyField(Mtech, help_text=' (Press Ctrl to select multiple)')
    invitees_phd = models.ManyToManyField(PhD)
    # invitees_btech = models.ManyToManyField(Btech, help_text=' (Press Ctrl to select multiple)')
    def __str__(self):
        return self.name


class Poll(models.Model):

    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
    response_coming = models.PositiveIntegerField()
    response_not_coming  = models.PositiveIntegerField()
    response_not_sure = models.PositiveIntegerField()




