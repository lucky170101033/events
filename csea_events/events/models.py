from django.db import models
import uuid

from django.contrib.auth.models import User

# Create your models here.

class Event(models.Model):

    # todo, extend and test by sunday

    name = models.CharField(max_length=300, help_text='Enter the event name')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular event')
    fee = models.PositiveIntegerField()
    capacity  = models.PositiveIntegerField()
    target_audience = models.CharField(max_length=300)
    date = models.DateField(null = False, blank = False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    faq = models.TextField()
    tags = models.CharField(max_length=300)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    invitees = models.CharField(max_length=50)


    def __str__(self):
        return self.name


# class Poll(models.Model):
#     #TO be tested and debugged by sunday
#     event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
#     response_coming = models.PositiveIntegerField()
#     response_not_coming  = models.PositiveIntegerField()
#     response_not_sure = models.PositiveIntegerField()

#     class Meta:
#         verbose_name = _("Poll")
#         verbose_name_plural = _("Polls")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("Poll_detail", kwargs={"pk": self.pk})
