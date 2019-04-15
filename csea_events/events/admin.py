from django.contrib import admin
from events.models import Event, Btech, Mtech, PhD
# Register your models here.

admin.site.register(Event)

admin.site.register(Btech)

admin.site.register(Mtech)

admin.site.register(PhD)